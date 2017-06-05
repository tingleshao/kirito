# adjust the order of the cameras in an pto file, try to get the best possbile
# stitching result


def adjust_order_for_mantis_cam4(input_pto_file_name, output_pto_file_name):
    with open(input_pto_file_name) as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    cam_info_dict = {}
    output_str = ""
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if len(line) > 20 and line[-6:-1] == ".jpeg":
            cam_info_dict[line[-9:-1].split(".")[0]] = line
        curr_idx = curr_idx + 1
    curr_idx = 0
    curr_idx_for_cam = 0
    cam_list = ["410","409","408","407","406","400","401","402","403","404","405","411","417","416","415","414","413","412","418"]
    # rewrite pto file
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if len(line) > 20 and line[-6:-1] == ".jpeg":
            output_str = output_str + cam_info_dict[cam_list[curr_idx_for_cam]] + "\n"
        else:
            output_str = output_str + line + "\n"
    # write output
    with open("output_pto_file_name", 'w') as output_file:
        output_file.write(output_str)


if __name__ == "__main__":
    adjust_order_for_mantis_cam4("foo", "bar")
