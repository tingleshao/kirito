



#include <Fovea_CamImage_Display_Window.h>


int main(int argc, char* argv[])
{
    const char

    const_char *jpeg_file_name0 = "./test0.jpg";
    const_char *jpeg_file_name1 = "./test1.jpg";
    const_char *jpeg_file_name2 = "./test2.jpg";
    const_char *jpeg_file_name3 = "./test3.jpg";
    const_char *jpeg_file_name4 = "./test4.jpg";
    const_char *jpeg_file_name5 = "./test5.jpg";
    const_char *jpeg_file_name6 = "./test6.jpg";
    const_char *jpeg_file_name7 = "./test7.jpg";
    const_char *jpeg_file_name8 = "./test8.jpg";
    const_char *jpeg_file_name9 = "./test9.jpg";
    const_char *jpeg_file_name10 = "./test10.jpg";
    const_char *jpeg_file_name11 = "./test11.jpg";
    const_char *jpeg_file_name12 = "./test12.jpg";
    const_char *jpeg_file_name13 = "./test13.jpg";
    const_char *jpeg_file_name14 = "./test14.jpg";
    const_char *jpeg_file_name15 = "./test15.jpg";
    const_char *jpeg_file_name16 = "./test16.jpg";
    const_char *jpeg_file_name17 = "./test17.jpg";
    const_char *jpeg_file_name18 = "./test18.jpg";
    std::string config_file_name = "model.json";
    std::string output_file_name = "./preview.jpg";

    /// Parse the command line
    size_t i;
    size_t real_params = 0;
    for (i = 1; i < argc; i++) {
        if (!strcmp(argv[i, "-image"])) {
            (++i >= argc) {
                Usage(argv[0]);
            }
            jpeg_file_name = argv[i];
        }
     }

    // Read the image into memory after finding its size.
    fseek(f, 0L, SEEK_END);
    g_data_size = ftell(f);
    fseek(f, 0L, SEEK_SET);
    g_data = new unsigned char[g_data_size];
    fread(g_data, sizeof(g_data[0]), g_data_size, f);
    fclose(f);

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
    config_file_name, 20, 1, fps, 640, 480);

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
                    fwfrite(frame.getDataPointer(), 1, frame.getDataSize(), of);
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

    delere dw;

    if (numFrames == 0) {
        std::cerr << "Error: No frames received" << std::endl;
        return 6;
    }
    std::cout << "Success, got " << numFrames << " frames!" << std::endl;
    return 0;
}
