# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/cshao/dev/agt/build/fovea-prefix/src/fovea

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build

# Include any dependencies generated for this target.
include FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/depend.make

# Include the progress variables for this target.
include FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/progress.make

# Include the compile flags for this target's objects.
include FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/flags.make

FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o: FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/flags.make
FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o: /home/cshao/dev/agt/build/fovea-prefix/src/fovea/FoveaRenderLib/Kirito_rendering.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/cshao/dev/agt/build/fovea-prefix/src/fovea-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o"
	cd /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build/FoveaRenderLib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o -c /home/cshao/dev/agt/build/fovea-prefix/src/fovea/FoveaRenderLib/Kirito_rendering.cpp

FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.i"
	cd /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build/FoveaRenderLib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/cshao/dev/agt/build/fovea-prefix/src/fovea/FoveaRenderLib/Kirito_rendering.cpp > CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.i

FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.s"
	cd /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build/FoveaRenderLib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/cshao/dev/agt/build/fovea-prefix/src/fovea/FoveaRenderLib/Kirito_rendering.cpp -o CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.s

FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o.requires:

.PHONY : FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o.requires

FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o.provides: FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o.requires
	$(MAKE) -f FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/build.make FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o.provides.build
.PHONY : FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o.provides

FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o.provides.build: FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o


# Object files for target Kirito_rendering
Kirito_rendering_OBJECTS = \
"CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o"

# External object files for target Kirito_rendering
Kirito_rendering_EXTERNAL_OBJECTS =

FoveaRenderLib/Kirito_rendering: FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o
FoveaRenderLib/Kirito_rendering: FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/build.make
FoveaRenderLib/Kirito_rendering: FoveaRenderLib/libFoveaEnvisionLib.a
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libglfw.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXrandr.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXxf86vm.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXcursor.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXinerama.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXi.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libSM.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libICE.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libX11.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXext.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libGLEW.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libGLU.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libGL.so
FoveaRenderLib/Kirito_rendering: FoveaImagePipelineLib/libFoveaImagePipelineLib.a
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libGLEW.so
FoveaRenderLib/Kirito_rendering: /usr/local/cuda-8.0/lib64/libcudart_static.a
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/librt.so
FoveaRenderLib/Kirito_rendering: /home/cshao/dev/agt/build/INSTALL/lib/libvrpn.a
FoveaRenderLib/Kirito_rendering: /home/cshao/dev/agt/build/INSTALL/lib/libAPLFrame.a
FoveaRenderLib/Kirito_rendering: /home/cshao/dev/agt/build/INSTALL/lib/libatl.a
FoveaRenderLib/Kirito_rendering: /usr/local/lib/libJsonBox.a
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libcuda.so
FoveaRenderLib/Kirito_rendering: /usr/local/cuda-8.0/lib64/libcudart_static.a
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/librt.so
FoveaRenderLib/Kirito_rendering: /home/cshao/dev/agt/build/INSTALL/lib/libvrpn.a
FoveaRenderLib/Kirito_rendering: /home/cshao/dev/agt/build/INSTALL/lib/libAPLFrame.a
FoveaRenderLib/Kirito_rendering: /home/cshao/dev/agt/build/INSTALL/lib/libatl.a
FoveaRenderLib/Kirito_rendering: /usr/local/lib/libJsonBox.a
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libcuda.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libGLU.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libGL.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libnvcuvid.so
FoveaRenderLib/Kirito_rendering: /home/cshao/dev/agt/build/INSTALL/lib/libvrpnserver.a
FoveaRenderLib/Kirito_rendering: /home/cshao/dev/agt/build/INSTALL/lib/libquat.a
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libjpeg.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libglfw.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXrandr.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXxf86vm.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXcursor.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXinerama.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXi.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libSM.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libICE.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libX11.so
FoveaRenderLib/Kirito_rendering: /usr/lib/x86_64-linux-gnu/libXext.so
FoveaRenderLib/Kirito_rendering: FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/cshao/dev/agt/build/fovea-prefix/src/fovea-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Kirito_rendering"
	cd /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build/FoveaRenderLib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Kirito_rendering.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/build: FoveaRenderLib/Kirito_rendering

.PHONY : FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/build

FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/requires: FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/Kirito_rendering.cpp.o.requires

.PHONY : FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/requires

FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/clean:
	cd /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build/FoveaRenderLib && $(CMAKE_COMMAND) -P CMakeFiles/Kirito_rendering.dir/cmake_clean.cmake
.PHONY : FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/clean

FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/depend:
	cd /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/cshao/dev/agt/build/fovea-prefix/src/fovea /home/cshao/dev/agt/build/fovea-prefix/src/fovea/FoveaRenderLib /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build/FoveaRenderLib /home/cshao/dev/agt/build/fovea-prefix/src/fovea-build/FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : FoveaRenderLib/CMakeFiles/Kirito_rendering.dir/depend

