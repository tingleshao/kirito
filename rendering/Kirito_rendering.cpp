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
int g_image_width = 3840;
int g_image_height = 2160;

const char *jpeg_file_name0;
const char *jpeg_file_name1;
const char *jpeg_file_name2;
const char *jpeg_file_name3;
const char *jpeg_file_name4;
const char *jpeg_file_name5 ;
const char *jpeg_file_name6 ;
const char *jpeg_file_name7;
const char *jpeg_file_name8 ;
const char *jpeg_file_name9;
const char *jpeg_file_name10;
const char *jpeg_file_name11 ;
const char *jpeg_file_name12;
const char *jpeg_file_name13;
const char *jpeg_file_name14;
const char *jpeg_file_name15;
const char *jpeg_file_name16 ;
const char *jpeg_file_name17;
const char *jpeg_file_name18;

static atl::CamImage RequestImageHandler(void *userdata, const Fovea_ATL_image_request &request) {
  //  const char *jpeg_file_name0 = "./test0.jpg";
  //  const char *jpeg_file_name1 = "./test1.jpg";
    unsigned char *g_data0 = nullptr;
    size_t g_data_size0 = 0;
    unsigned char *g_data1 = nullptr;
    size_t g_data_size1 = 0;
    unsigned char *g_data2 = nullptr;
    size_t g_data_size2 = 0;
    unsigned char *g_data3 = nullptr;
    size_t g_data_size3 = 0;
    unsigned char *g_data4 = nullptr;
    size_t g_data_size4 = 0;
    unsigned char *g_data5 = nullptr;
    size_t g_data_size5 = 0;
    unsigned char *g_data6 = nullptr;
    size_t g_data_size6 = 0;
    unsigned char *g_data7 = nullptr;
    size_t g_data_size7 = 0;
    unsigned char *g_data8 = nullptr;
    size_t g_data_size8 = 0;
    unsigned char *g_data9 = nullptr;
    size_t g_data_size9 = 0;
    unsigned char *g_data10 = nullptr;
    size_t g_data_size10 = 0;
    unsigned char *g_data11 = nullptr;
    size_t g_data_size11 = 0;
    unsigned char *g_data12 = nullptr;
    size_t g_data_size12 = 0;
    unsigned char *g_data13 = nullptr;
    size_t g_data_size13 = 0;
    unsigned char *g_data14 = nullptr;
    size_t g_data_size14 = 0;
    unsigned char *g_data15 = nullptr;
    size_t g_data_size15 = 0;
    unsigned char *g_data16 = nullptr;
    size_t g_data_size16 = 0;
    unsigned char *g_data17 = nullptr;
    size_t g_data_size17 = 0;
    unsigned char *g_data18 = nullptr;
    size_t g_data_size18 = 0;

    atl::CamImage ret;

    if (request.d_camId == 1021700000) {

        FILE *f = fopen(jpeg_file_name0, "rb");
        if (!f) {
            std::cerr << "Could not open JPEG file " << jpeg_file_name0 << std::endl;
        }

        // Read the image into memory after finding its size.
        fseek(f, 0L, SEEK_END);
        g_data_size0 = ftell(f);
        fseek(f, 0L, SEEK_SET);
        g_data0 = new unsigned char[g_data_size0];
        fread(g_data0, sizeof(g_data0[0]), g_data_size0, f);
        fclose(f);

        ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size0);
    } else if (request.d_camId == 1021700002) {
      FILE *f1 = fopen(jpeg_file_name1, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name1 << std::endl;
      }
          fseek(f1, 0L, SEEK_END);
          g_data_size1 = ftell(f1);
          fseek(f1, 0L, SEEK_SET);
          g_data1 = new unsigned char[g_data_size1];
          fread(g_data1, sizeof(g_data1[0]), g_data_size1, f1);
          fclose(f1);
          ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size1);

    }  else if (request.d_camId == 1021700004) {
      FILE *f1 = fopen(jpeg_file_name2, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name2 << std::endl;
      }

      fseek(f1, 0L, SEEK_END);
      g_data_size2 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data2 = new unsigned char[g_data_size2];
      fread(g_data2, sizeof(g_data2[0]), g_data_size2, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size2);
    }  else if (request.d_camId == 1021700005) {
      FILE *f1 = fopen(jpeg_file_name3, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name3 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size3 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data3 = new unsigned char[g_data_size3];
      fread(g_data3, sizeof(g_data3[0]), g_data_size3, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size3);
    }  else if (request.d_camId == 1021700006) {
      FILE *f1 = fopen(jpeg_file_name4, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name4 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size4 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data4 = new unsigned char[g_data_size4];
      fread(g_data4, sizeof(g_data4[0]), g_data_size4, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size4);
    }  else if (request.d_camId == 1021700007) {
      FILE *f1 = fopen(jpeg_file_name5, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name5 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size5 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data5 = new unsigned char[g_data_size5];
      fread(g_data5, sizeof(g_data5[0]), g_data_size5, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size5);
    }  else if (request.d_camId == 1021700008) {
      FILE *f1 = fopen(jpeg_file_name6, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name6 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size6 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data6 = new unsigned char[g_data_size6];
      fread(g_data6, sizeof(g_data6[0]), g_data_size6, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size6);
    }  else if (request.d_camId == 1021700009) {
      FILE *f1 = fopen(jpeg_file_name7, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name7 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size7 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data7 = new unsigned char[g_data_size7];
      fread(g_data1, sizeof(g_data7[0]), g_data_size7, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size7);
    }  else if (request.d_camId == 1021700010) {
      FILE *f1 = fopen(jpeg_file_name8, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name8 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size8 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data8 = new unsigned char[g_data_size8];
      fread(g_data8, sizeof(g_data8[0]), g_data_size8, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size8);
    }  else if (request.d_camId == 1021700011) {
      FILE *f1 = fopen(jpeg_file_name9, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name9 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size9 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data9 = new unsigned char[g_data_size9];
      fread(g_data9, sizeof(g_data9[0]), g_data_size9, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size9);
    }  else if (request.d_camId == 1021700014) {
      FILE *f1 = fopen(jpeg_file_name10, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name10 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size10 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data10 = new unsigned char[g_data_size10];
      fread(g_data10, sizeof(g_data10[0]), g_data_size10, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size10);
    }  else if (request.d_camId == 1021700016) {
      FILE *f1 = fopen(jpeg_file_name11, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name11 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size11 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data11 = new unsigned char[g_data_size11];
      fread(g_data11, sizeof(g_data11[0]), g_data_size11, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size11);
    }  else if (request.d_camId == 1021700018) {
      FILE *f1 = fopen(jpeg_file_name12, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name12 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size12 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data12 = new unsigned char[g_data_size12];
      fread(g_data12, sizeof(g_data12[0]), g_data_size12, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size12);
    }  else if (request.d_camId == 1021700019) {
      FILE *f1 = fopen(jpeg_file_name13, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name13 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size13 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data13 = new unsigned char[g_data_size13];
      fread(g_data13, sizeof(g_data13[0]), g_data_size13, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size13);
    }  else if (request.d_camId == 1021700021) {
      FILE *f1 = fopen(jpeg_file_name14, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name14 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size14 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data14 = new unsigned char[g_data_size14];
      fread(g_data14, sizeof(g_data14[0]), g_data_size14, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size14);
    }  else if (request.d_camId == 1021700026) {
      FILE *f1 = fopen(jpeg_file_name15, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name15 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size15 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data15 = new unsigned char[g_data_size15];
      fread(g_data15, sizeof(g_data15[0]), g_data_size15, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size15);
    }  else if (request.d_camId == 1031700003) {
      FILE *f1 = fopen(jpeg_file_name16, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name16 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size16 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data16 = new unsigned char[g_data_size16];
      fread(g_data16, sizeof(g_data1[0]), g_data_size16, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size16);
    }  else if (request.d_camId == 1031700030) {
      FILE *f1 = fopen(jpeg_file_name17, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name17 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size17 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data17 = new unsigned char[g_data_size17];
      fread(g_data17, sizeof(g_data17[0]), g_data_size17, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size17);
    }  else if (request.d_camId == 18) {
      FILE *f1 = fopen(jpeg_file_name18, "rb");
      if (!f1) {
         std::cerr << "Could not open JPEG file " << jpeg_file_name18 << std::endl;
      }
      fseek(f1, 0L, SEEK_END);
      g_data_size18 = ftell(f1);
      fseek(f1, 0L, SEEK_SET);
      g_data18 = new unsigned char[g_data_size18];
      fread(g_data18, sizeof(g_data18[0]), g_data_size18, f1);
      fclose(f1);
      ret.allocate(g_image_width, g_image_height, 24, ATL_MODE_JPEG_RGB, g_data_size18);
    }

    uint8_t *writePointer;
    if (!ret.getWritePointer(&writePointer)) {
        std::cerr << "RequestImageHandler(): Could not get write pointer" << std::endl;
    } else {
        if (request.d_camId == 1021700000 ) {
            memcpy(writePointer, g_data0, g_data_size0);
            ret.lockWritePointer(&writePointer, g_data_size0);
        }
        else if (request.d_camId == 1021700002) {
          memcpy(writePointer, g_data1, g_data_size1);
          ret.lockWritePointer(&writePointer, g_data_size1);
        } else if (request.d_camId == 1021700004 ) {
              memcpy(writePointer, g_data2, g_data_size2);
              ret.lockWritePointer(&writePointer, g_data_size2);
        } else if (request.d_camId == 1021700005 ) {
              memcpy(writePointer, g_data3, g_data_size3);
              ret.lockWritePointer(&writePointer, g_data_size3);
        } else if (request.d_camId == 1021700006 ) {
              memcpy(writePointer, g_data4, g_data_size4);
              ret.lockWritePointer(&writePointer, g_data_size4);
        } else if (request.d_camId == 1021700007 ) {
              memcpy(writePointer, g_data5, g_data_size5);
              ret.lockWritePointer(&writePointer, g_data_size5);
        } else if (request.d_camId == 1021700008 ) {
              memcpy(writePointer, g_data6, g_data_size6);
              ret.lockWritePointer(&writePointer, g_data_size6);
        } else if (request.d_camId == 1021700009 ) {
              memcpy(writePointer, g_data7, g_data_size7);
              ret.lockWritePointer(&writePointer, g_data_size7);
        } else if (request.d_camId == 1021700010 ) {
              memcpy(writePointer, g_data8, g_data_size8);
              ret.lockWritePointer(&writePointer, g_data_size8);
        } else if (request.d_camId == 1021700011 ) {
                            memcpy(writePointer, g_data9, g_data_size9);
                            ret.lockWritePointer(&writePointer, g_data_size9);
                        } else if (request.d_camId == 1021700014 ) {
                              memcpy(writePointer, g_data10, g_data_size10);
                              ret.lockWritePointer(&writePointer, g_data_size10);
                          } else if (request.d_camId == 1021700016 ) {
                                memcpy(writePointer, g_data11, g_data_size11);
                                ret.lockWritePointer(&writePointer, g_data_size11);
                            } else if (request.d_camId == 1021700018 ) {
                                  memcpy(writePointer, g_data12, g_data_size12);
                                  ret.lockWritePointer(&writePointer, g_data_size12);
                              } else if (request.d_camId == 1021700019 ) {
                                    memcpy(writePointer, g_data13, g_data_size13);
                                    ret.lockWritePointer(&writePointer, g_data_size13);
                                } else if (request.d_camId == 1021700021 ) {
                                      memcpy(writePointer, g_data14, g_data_size14);
                                      ret.lockWritePointer(&writePointer, g_data_size14);
                                  } else if (request.d_camId == 1021700026 ) {
                                        memcpy(writePointer, g_data15, g_data_size15);
                                        ret.lockWritePointer(&writePointer, g_data_size15);
                                    } else if (request.d_camId == 1031700003 ) {
                                          memcpy(writePointer, g_data16, g_data_size16);
                                          ret.lockWritePointer(&writePointer, g_data_size16);
                                      } else if (request.d_camId == 1031700030 ) {
                                            memcpy(writePointer, g_data17, g_data_size17);
                                            ret.lockWritePointer(&writePointer, g_data_size17);
                                        } else if (request.d_camId == 18 ) {
                                              memcpy(writePointer, g_data18, g_data_size18);
                                              ret.lockWritePointer(&writePointer, g_data_size18);
                                            }
    }
    // uint8_t *writePointer1;
    // if (!ret.getWritePointer(&writePointer1)) {
    //     std::cerr << "RequestImageHandler(): Could not get write pointer1" << std::endl;
    // } else {
    //     if (request.d_camId == 1021700000 ) {
    //         memcpy(writePointer, g_data0, g_data_size0);
    //         ret.lockWritePointer(&writePointer, g_data_size0);
    //     }
    //   }
    //   uint8_t *writePointer2;
    //   if (!ret.getWritePointer(&writePointer2)) {
    //       std::cerr << "RequestImageHandler(): Could not get write pointer2" << std::endl;
    //   } else {
    //       if (request.d_camId == 1021700000 ) {
    //           memcpy(writePointer2, g_data0, g_data_size0);
    //           ret.lockWritePointer(&writePointer,2 g_data_size0);
    //       }
    //     }
    //     else if (request.d_camId == 1021700002) {
    //       memcpy(writePointer, g_data1, g_data_size1);
    //       ret.lockWritePointer(&writePointer, g_data_size1);
    //     } else if (request.d_camId == 1021700004 ) {
    //           memcpy(writePointer, g_data2, g_data_size2);
    //           ret.lockWritePointer(&writePointer, g_data_size2);
    //       } else if (request.d_camId == 1021700005 ) {
    //             memcpy(writePointer, g_data3, g_data_size3);
    //             ret.lockWritePointer(&writePointer, g_data_size3);
    //         } else if (request.d_camId == 1021700006 ) {
    //               memcpy(writePointer, g_data4, g_data_size4);
    //               ret.lockWritePointer(&writePointer, g_data_size4);
    //           } else if (request.d_camId == 1021700007 ) {
    //                 memcpy(writePointer, g_data5, g_data_size5);
    //                 ret.lockWritePointer(&writePointer, g_data_size5);
    //             } else if (request.d_camId == 1021700008 ) {
    //                   memcpy(writePointer, g_data6, g_data_size6);
    //                   ret.lockWritePointer(&writePointer, g_data_size6);
    //               } else if (request.d_camId == 1021700009 ) {
    //                     memcpy(writePointer, g_data7, g_data_size7);
    //                     ret.lockWritePointer(&writePointer, g_data_size7);
    //                 } else if (request.d_camId == 1021700010 ) {
    //                       memcpy(writePointer, g_data8, g_data_size8);
    //                       ret.lockWritePointer(&writePointer, g_data_size8);
    //                   } else if (request.d_camId == 1021700011 ) {
    //                         memcpy(writePointer, g_data9, g_data_size9);
    //                         ret.lockWritePointer(&writePointer, g_data_size9);
    //                     } else if (request.d_camId == 1021700014 ) {
    //                           memcpy(writePointer, g_data10, g_data_size10);
    //                           ret.lockWritePointer(&writePointer, g_data_size10);
    //                       } else if (request.d_camId == 1021700016 ) {
    //                             memcpy(writePointer, g_data11, g_data_size11);
    //                             ret.lockWritePointer(&writePointer, g_data_size11);
    //                         } else if (request.d_camId == 1021700018 ) {
    //                               memcpy(writePointer, g_data12, g_data_size12);
    //                               ret.lockWritePointer(&writePointer, g_data_size12);
    //                           } else if (request.d_camId == 1021700019 ) {
    //                                 memcpy(writePointer, g_data13, g_data_size13);
    //                                 ret.lockWritePointer(&writePointer, g_data_size13);
    //                             } else if (request.d_camId == 1021700021 ) {
    //                                   memcpy(writePointer, g_data14, g_data_size14);
    //                                   ret.lockWritePointer(&writePointer, g_data_size14);
    //                               } else if (request.d_camId == 1021700026 ) {
    //                                     memcpy(writePointer, g_data15, g_data_size15);
    //                                     ret.lockWritePointer(&writePointer, g_data_size15);
    //                                 } else if (request.d_camId == 1031700003 ) {
    //                                       memcpy(writePointer, g_data16, g_data_size16);
    //                                       ret.lockWritePointer(&writePointer, g_data_size16);
    //                                   } else if (request.d_camId == 1031700030 ) {
    //                                         memcpy(writePointer, g_data17, g_data_size17);
    //                                         ret.lockWritePointer(&writePointer, g_data_size17);
    //                                     } else if (request.d_camId == 18 ) {
    //                                           memcpy(writePointer, g_data18, g_data_size18);
    //                                           ret.lockWritePointer(&writePointer, g_data_size18);
    //                                         }
    // }
    ret.setGamma(2.4);
    ret.setShutter(1e-3f);

    return ret;
}

static uint64_t RequestLargestTimeHandler(void *userdata, uint64_t camera_id) {
    return 1000;
}

int main(int argc, char* argv[])
{
  number_of_jpeg = argv[1]
  int i;
  for (i = 0; i < number_of_jpeg; i++) {}
    jpeg_file_name0 = argv[i+2];
    jpeg_file_name1 = argv[2];
    jpeg_file_name2 = argv[3];
    jpeg_file_name3 = argv[4];
   jpeg_file_name4 = argv[5];
     jpeg_file_name5 = argv[6];
     jpeg_file_name6 = argv[7];
   jpeg_file_name7 = argv[8];
     jpeg_file_name8 = argv[9];
   jpeg_file_name9 = argv[10];
     jpeg_file_name10 = argv[11];
   jpeg_file_name11 = argv[12];
     jpeg_file_name12 = argv[13];
     jpeg_file_name13 = argv[14];
     jpeg_file_name14 = argv[15];
     jpeg_file_name15 = argv[16];
     jpeg_file_name16 = argv[17];
     jpeg_file_name17 = argv[18];
     jpeg_file_name18 = argv[19];
    std::string config_file_name = "model.json";
    std::string output_file_name = "./preview.jpg";

    double fps = 2;
    bool verbose = false;
    double duration = 3;

    /// Parse the command line
    size_t i;
    size_t real_params = 0;

    // Test the image returning callback handler.
    Fovea_ATL_image_request testReq(18,0,1);
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
