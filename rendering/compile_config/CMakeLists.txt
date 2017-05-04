cmake_minimum_required(VERSION 2.6)
project(FoveaRender)

#-----------------------------------------------------------------------------
# On Windows 7, it does not work to install in the default location,
# which is the Program Files directory, because you have to not only have
# file permission to write there but also "run as administrator."  This
# means that "make install" from a Visual Studio project fails.  To get
# around that, we need to set CMAKE_INSTALL_PREFIX to something other
# than the default.  However, it is a cache variable that has already been
# set.  If we make a local variable, it uses this rather than the cache
# variable and never tells the poor user what happened (the GUI location
# looks standard but the files end up somewhere else).  If we make it a
# non-forced cache variable, it already has a value so does not change.
# If we make it a forced cache variable, it gets overwritten every time
# and the user cannot change it on the GUI.  So we have a workaround here.
# We make a cache variable that records whether we have ever forced the
# install prefix.  If not, we force it.  If so, we don't force it again.
# This has the effect of setting it the first time cmake is run, showing
# the change in the GUI, and also letting the user change the value in
# the GUI if they don't like what we did.  If I knew how to do this only
# happen on Windows 7, I'd make the if(WIN32) more specific.
if(WIN32 AND NOT SUBPROJECT)
    if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT
        AND
        (NOT
        ONCE_SET_CMAKE_INSTALL_PREFIX))
        set(ONCE_SET_CMAKE_INSTALL_PREFIX
            true
            CACHE
            INTERNAL
            "Have we set the install prefix yet?"
            FORCE)
        set(CMAKE_INSTALL_PREFIX
            C:/usr/local
            CACHE
            PATH
            "Install path prefix, prepended onto install directories"
            FORCE)
    endif()
endif()

#-----------------------------------------------------------------------------
# Local CMake Modules
list(APPEND CMAKE_MODULE_PATH ${FoveaRender_SOURCE_DIR} ${FoveaRender_SOURCE_DIR}/cmake)

#-----------------------------------------------------------------------------
# Libraries that we need.
FIND_PACKAGE(VRPN REQUIRED)
FIND_PACKAGE(quatlib REQUIRED)
FIND_PACKAGE(libjpeg REQUIRED)  # Nested dependency on APL
FIND_PACKAGE(APL REQUIRED)
find_package(GLFW)
if (GLFW_FOUND)
    include_directories(${GLFW_INCLUDE_DIR})
endif()

#-----------------------------------------------------------------------------
# Include directory needed by all of the files
include_directories(SYSTEM
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${VRPN_INCLUDE_DIR}
  ${QUATLIB_INCLUDE_DIR}
  ${LIBJPEG_INCLUDE_DIR}
)
# For Fovea_Configure.h
include_directories(${PROJECT_BINARY_DIR}/../FoveaImagePipelineLib)

#-----------------------------------------------------------------------------
# Helper for dependencies

include(GNUInstallDirs)
# Win-specific: we want shared libs (dlls) in same dir as exe files.
if(WIN32)
	set(FOVEAREN_SHARED_LIBRARY_DIR "${CMAKE_INSTALL_BINDIR}")
else()
	set(FOVEAREN_SHARED_LIBRARY_DIR "${CMAKE_INSTALL_LIBDIR}")
endif()

include(CopyImportedTarget)
## Copy and install shared libraries from imported targets as required.
## Also generate a list of imported targets for clients of RM to make use of.
get_filename_component(FOVEAREN_REQUIRED_LIBRARIES_DIR "${FOVEAREN_SHARED_LIBRARY_DIR}" ABSOLUTE BASE_DIR "${CMAKE_INSTALL_PREFIX}")
get_filename_component(FOVEAREN_CONFIG_INSTALL_DIR "${CONFIG_INSTALL_DIR}" ABSOLUTE BASE_DIR "${CMAKE_INSTALL_PREFIX}")
file(RELATIVE_PATH FOVEAREN_REQUIRED_LIBRARIES_DIR "${FOVEAREN_CONFIG_INSTALL_DIR}" "${FOVEAREN_REQUIRED_LIBRARIES_DIR}/.")

set(FOVEAREN_REQUIRED_LIBRARIES_DEBUG)
set(FOVEAREN_REQUIRED_LIBRARIES_RELEASE)
set(FOVEAREN_REQUIRED_LIBRARIES_RELWITHDEBINFO)
set(FOVEAREN_REQUIRED_LIBRARIES_MINSIZEREL)
function(fovearen_copy_deps)
	copy_imported_targets(FoveaRenderLib ${ARGN})
	foreach(_dep ${ARGN})
		install_imported_target(${_dep} DESTINATION ${FOVEAREN_SHARED_LIBRARY_DIR} COMPONENT Runtime)
		foreach(_config DEBUG RELEASE RELWITHDEBINFO MINSIZEREL)
			get_target_property(_lib_location ${_dep} LOCATION_${_config})
			get_filename_component(_lib_filename "${_lib_location}" NAME)
			set(_lib_filename "${FOVEAREN_REQUIRED_LIBRARIES_DIR}/${_lib_filename}")
			list(APPEND FOVEAREN_REQUIRED_LIBRARIES_${_config} "${_lib_filename}")
			set(FOVEAREN_REQUIRED_LIBRARIES_${_config} "${FOVEAREN_REQUIRED_LIBRARIES_${_config}}" PARENT_SCOPE)
		endforeach()
	endforeach()
endfunction()

#-----------------------------------------------------------------------------
# Build the library itself and declare what bits need to be installed
set(FoveaRenderLib_SOURCES
    Fovea_binner.cpp
)
set(FoveaRenderLib_HEADER
    Fovea_binner.h
)

add_library(FoveaRenderLib ${FoveaRenderLib_SOURCES} ${FoveaRenderLib_HEADER})
set_property(TARGET FoveaRenderLib PROPERTY PUBLIC_HEADER ${FoveaRenderLib_HEADER})
target_include_directories(FoveaRenderLib SYSTEM
    INTERFACE $<BUILD_INTERFACE:${FoveaRender_SOURCE_DIR}>)
target_link_libraries(FoveaRenderLib PUBLIC ${APL_LIBRARIES})
fovea_install_exported_targets(
    TARGETS FoveaRenderLib
    DEPENDS APL)

#-----------------------------------------------------------------------------
#Build the testapps if required
option(FoveaRender_BUILD_TESTS "Enable to build FoveaRender tests" ON)

if(FoveaRender_BUILD_TESTS)

    set(CPPAPPS
        Fovea_binner_test
        )

    foreach(APP ${CPPAPPS})
        add_executable(${APP} ${APP}.cpp)
        target_link_libraries(${APP}
            FoveaRenderLib
        )

        if(WIN32)       # MS-Windows, both 32 and 64 bits
            target_link_libraries(${APP} wsock32)
        elseif(APPLE)   # Apple
            target_link_libraries(${APP} m)	# Math library
        elseif(UNIX)    # other UNIXes
            target_link_libraries(${APP} m)	# Math library
        endif()

    endforeach()

    #-----------------------------------------------------------------------------
    # Enable CTest
    enable_testing()
    add_test(Fovea_binner_test Fovea_binner_test)

endif()

#-----------------------------------------------------------------------------
# Libraries that we need and can use for FoveaEnvisionLib.
FIND_PACKAGE(OpenGL)
FIND_PACKAGE(GLEW)
find_package(OpenMP)
if (OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

if(GLFW_FOUND)
  set(Envision_GLFW_SOURCES
    Fovea_CamImage_Display_Window.cpp
  )
  set(Envision_GLFW_HEADERS
    Fovea_CamImage_Display_Window.h
  )
endif()

if(OPENGL_FOUND AND GLEW_FOUND)

  fovearen_copy_deps(GLEW::GLEW)

  #-----------------------------------------------------------------------------
  # Include directory needed by all of the files
  include_directories(SYSTEM ${OPENGL_INCLUDE_DIR} ${GLEW_INCLUDE_DIR})

  #-----------------------------------------------------------------------------
  # Build the library itself and declare what bits need to be installed
  set(FoveaEnvisionLib_SOURCES
    Fovea_shaders.cpp
    Fovea_microcamera_renderers.cpp
    Fovea_GL_buffer_pool.cpp
    Fovea_GL_buffer_hierarchy.cpp
    Fovea_GL_buffer_predictive_decompressor.cpp
    Fovea_CamImage_GL_buffer_predictive_decompressor.cpp
    ${Envision_GLFW_SOURCES}
#    Fovea_texture_manager.cpp
  )
  set(FoveaEnvisionLib_HEADER
    Fovea_shaders.h
    Fovea_microcamera_renderers.h
    Fovea_GL_buffer_pool.h
    Fovea_GL_buffer_hierarchy.h
    Fovea_GL_buffer_predictive_decompressor.h
    Fovea_CamImage_GL_buffer_predictive_decompressor.h
    ${Envision_GLFW_HEADERS}
#    Fovea_texture_manager.h
  )

  add_library(FoveaEnvisionLib ${FoveaEnvisionLib_SOURCES} ${FoveaEnvisionLib_HEADER})
  set_property(TARGET FoveaEnvisionLib PROPERTY PUBLIC_HEADER ${FoveaEnvisionLib_HEADER})
  target_include_directories(FoveaEnvisionLib SYSTEM
    INTERFACE $<BUILD_INTERFACE:${FoveaRender_SOURCE_DIR}>)
  target_link_libraries(FoveaEnvisionLib PUBLIC
    FoveaImagePipelineLib
    GLEW::GLEW
    ${OPENGL_LIBRARIES}
    ${VRPN_SERVER_LIBRARIES}
    ${QUATLIB_LIBRARIES}
    ${LIBJPEG_LIBRARIES}
  )
  if(WIN32)
    # Required for the VRPN HID-based server libraries.
    target_link_libraries(FoveaEnvisionLib PUBLIC
      setupapi
    )
  else()
    # Required for the VRPN HID-based server libraries.
    target_link_libraries(FoveaEnvisionLib PUBLIC
      usb-1.0
    )
  endif()

  if(GLFW_FOUND)
    target_link_libraries(FoveaEnvisionLib PUBLIC
      ${GLFW_LIBRARIES}
    )
  endif()
  target_compile_features(FoveaEnvisionLib PUBLIC cxx_range_for)
  fovea_install_exported_targets(
    TARGETS FoveaEnvisionLib
    DEPENDS VRPN)

  #-----------------------------------------------------------------------------
  #Build the testapps if requested

  if (GLFW_FOUND AND GLEW_FOUND)
    # fovearen_copy_deps(${GLFW_LIBRARIES})
    set(GLFW_CPPAPPS
      Fovea_GL_buffer_pool_test
      Fovea_GL_buffer_hierarchy_test
      Fovea_GL_predictive_decompressor_test
      Fovea_CamImage_GL_predictive_decompressor_test
#        Fovea_shaders_test
        glfw_dual_window_example
        Fovea_microcamera_renderers_test
        Fovea_CamImage_Display_Window_test
        Fovea_CamImage_Display_Tiler_test
        Fovea_CamImage_Display_Jpeg_test
        Kirito_rendering
    )
    set(GLFW_LIBS ${GLFW_LIBRARIES})
  endif()

  if (FoveaImagePipeline_BUILD_FFMPEG)
    set(GLFW_CPPAPPS ${GLFW_CPPAPPS}
        Fovea_CamImage_Display_H264_test
    )
  endif()

  if(FoveaRender_BUILD_TESTS)

    set(CPPAPPS
#        Fovea_envision_common_test
        ${GLFW_CPPAPPS}
        )

    foreach(APP ${CPPAPPS})
        add_executable(${APP} ${APP}.cpp)
        target_link_libraries(${APP}
            FoveaEnvisionLib
            ${GLFW_LIBS}
            GLEW::GLEW
            ${OPENGL_LIBRARIES}
        )

        if(WIN32)       # MS-Windows, both 32 and 64 bits
            target_link_libraries(${APP} wsock32)
        elseif(APPLE)   # Apple
            target_link_libraries(${APP} m)	# Math library
        elseif(UNIX)    # other UNIXes
            target_link_libraries(${APP} m)	# Math library
        endif()

    endforeach()

    #-----------------------------------------------------------------------------
    # Enable CTest
    enable_testing()
#    add_test(Fovea_shaders_test Fovea_binner_test)

  endif()

endif()
