# Given a pto file, we displays the features detected, to see what is going on
#
#
#


def test():
    pto_file_name = "test3.pto"
    camera1_id = 1
    camera2_id = 2
    visualize_features_from_pto_files(pto_file_name, camera1_id, camera2_id)


if __name__ == "__main__":
    test()
