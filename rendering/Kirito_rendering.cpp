#ifdef _WIN32
#define _CRT_SECURE_NO_WARNINGS
#endif


#include <Fovea_CamImage_Display_Window.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <thread>
#include <chrono>


// Global variables to hold the info needed by the callback handlers

int g_image_width = 96;
int g_image_height = 96;

//int curr_frame_id = 0;

static atl::CamImage RequestImageHandler(void *userdata, const Fovea_ATL_image_request &request) {
    #if 0
     // a sfjalfjalfjasl
    #endif

    const char *jpeg_file_name0 = "./test0.jpg";
    const char *jpeg_file_name1 = "./test1.jpg";
    unsigned char *g_data = nullptr;
    size_t g_data_size = 0;
    unsigned char *g_data1 = nullptr;
    size_t g_data_size1 = 0;
    atl::CamImage ret;
    if (request.d_camId == 1 || request.d_camId == 2) {

        FILE *f = fopen(jpeg_file_name0, "rb");
        if (!f) {
            std::cerr << "Could not open JPEG file " << jpeg_file_name0 << std::endl;
        //    return 1;
        }

        // Read the image into memory after finding its size.
        fseek(f, 0L, SEEK_END);
        g_data_size = ftell(f);
        fseek(f, 0L, SEEK_SET);
        g_data = new unsigned char[g_data_size];
        fread(g_data, sizeof(g_data[0]), g_data_size, f);
        fclose(f);

        ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size);
      //  ret.setCamId(0);
    } else {
      FILE *f1 = fopen(jpeg_file_name1, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name1 << std::endl;
      //   return 1;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size1 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data1 = new unsigned char[g_data_size1];
      fread(g_data1, sizeof(g_data1[0]), g_data_size1, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size1);
      //    ret.setCamId(1);
    }

    uint8_t *writePointer;
    if (!ret.getWritePointer(&writePointer)) {
        std::cerr << "RequestImageHandler(): Could not get write pointer" << std::endl;
    } else {
        if (request.d_camId == 1 || request.d_camId == 2) {
            memcpy(writePointer, g_data, g_data_size);
            ret.lockWritePointer(&writePointer, g_data_size);
        }
        else {
          memcpy(writePointer, g_data1, g_data_size1);
          ret.lockWritePointer(&writePointer, g_data_size1);
        }
    }
    ret.setGamma(2.4);
    ret.setShutter(1e-3f);
//    curr_frame_id ++ ;
//    if (curr_frame_id == 2) {
//      curr_frame_id = 0;
//
    return ret;
}

static uint64_t RequestLargestTimeHandler(void *userdata, uint64_t camera_id) {
    return 1000;
}

int main(int argc, char* argv[])
{
    const char *jpeg_file_name0 = "./test0.jpg";
    const char *jpeg_file_name1 = "./test1.jpg";
    const char *jpeg_file_name2 = "./test2.jpg";
    const char *jpeg_file_name3 = "./test3.jpg";
    const char *jpeg_file_name4 = "./test4.jpg";
    const char *jpeg_file_name5 = "./test5.jpg";
    const char *jpeg_file_name6 = "./test6.jpg";
    const char *jpeg_file_name7 = "./test7.jpg";
    const char *jpeg_file_name8 = "./test8.jpg";
    const char *jpeg_file_name9 = "./test9.jpg";
    const char *jpeg_file_name10 = "./test10.jpg";
    const char *jpeg_file_name11 = "./test11.jpg";
    const char *jpeg_file_name12 = "./test12.jpg";
    const char *jpeg_file_name13 = "./test13.jpg";
    const char *jpeg_file_name14 = "./test14.jpg";
    const char *jpeg_file_name15 = "./test15.jpg";
    const char *jpeg_file_name16 = "./test16.jpg";
    const char *jpeg_file_name17 = "./test17.jpg";
    const char *jpeg_file_name18 = "./test18.jpg";
    std::string config_file_name = "model.json";
    std::string output_file_name = "./preview.jpg";

    double fps = 10;
    bool verbose = false;
    double duration = 0.5;

    /// Parse the command line
    size_t i;
    size_t real_params = 0;
  //  for (i = 1; i < argc; i++) {
  //      if (!strcmp(argv[i], "-image")) {
  //          (++i >= argc) {
  //              Usage(argv[0]);
  //          }
  //          jpeg_file_name = argv[i];
  ///      }
    // }

    // FILE *f = fopen(jpeg_file_name0, "rb");
    // if (!f) {
    //     std::cerr << "Could not open JPEG file " << jpeg_file_name0 << std::endl;
    //     return 1;
    // }
    //
    // FILE *f1 = fopen(jpeg_file_name1, "rb");
    // if (!f1) {
    //    std::cerr << "Could not open JPEG file " << jpeg_file_name1 << std::endl;
    //    return 1;
    // }
    //
    // // Read the image into memory after finding its size.
    // fseek(f, 0L, SEEK_END);
    // g_data_size = ftell(f);
    // fseek(f, 0L, SEEK_SET);
    // g_data = new unsigned char[g_data_size];
    // fread(g_data, sizeof(g_data[0]), g_data_size, f);
    // fclose(f);
    //
    // fseek(f1, 0L, SEEK_END);
    // g_data_size1 = ftell(f1);
    // fseek(f1, 0L, SEEK_SET);
    // g_data1 = new unsigned char[g_data_size1];
    //
    // fread(g_data1, sizeof(g_data1[0]), g_data_size1, f1);
    // fclose(f1);

    // Test the image returning callback handler.
    Fovea_ATL_image_request testReq(1,0,1);
    atl::CamImage testImage = RequestImageHandler(nullptr, testReq);
    if (testImage.getReadPointer() == nullptr) {
        std::cerr << "NULL data pointer in callback handler test, test code is broken" << std::endl;
        return 3;
    }
    if (testImage.getAllocatedDataSize() == 0) {
        std::cerr << "0 data size in callback handler test, test code is broken" << std::endl;
        return 4;
    }

    // Construct the Display Window we're going to use.
    Fovea_rendering_pose_state_PTZ state;
    Fovea_CamImage_semaphored_queue queue;
    Fovea_CamImage_Display_Jpeg *dw = new Fovea_CamImage_Display_Jpeg(queue, 100, state, RequestImageHandler, nullptr, RequestLargestTimeHandler, nullptr,
    config_file_name, 20, 1, fps, 640, 480, 180, false, true);

    // Wait...
    size_t numFrames = 0;
    auto start = std::chrono::system_clock::now();
    auto end = start;
    std::chrono::duration<double> dt = end - start;
    do {
        atl::CamImage frame;
        if (queue.pull(frame)) {
            if ((frame.getWidth() != 640) || (frame.getHeight() != 480)) {
                std::cerr << "Unexpected frame size: " << frame.getWidth() << "," << frame.getHeight() << std::endl;
                return 5;
            }

            if (output_file_name.size() > 0) {
                FILE *of = fopen(output_file_name.c_str(), "wb");
                if (of) {
                    fwrite(frame.getDataPointer(), 1, frame.getDataSize(), of);
                    fclose(of);
                } else {
                    std::cerr << "Could not open file " << output_file_name << "for writing" << std::endl;
                }
            }
            numFrames++;
        }
        end = std::chrono::system_clock::now();
        dt = end - start;
    } while ((duration == 0) || (dt.count() < duration));

    delete dw;

    if (numFrames == 0) {
        std::cerr << "Error: No frames received" << std::endl;
        return 6;
    }
    std::cout << "Success, got " << numFrames << " frames!" << std::endl;
    return 0;
}
