import matched
import cv2

# parse the plain text output into hugin style
# t he opencv feature extraction is on images with scale 581 x xxx
# hugin uses the original image resolution
# 2160 x xxxx
adjacernt_map = [[1, 8, 9, 10, 11, 12, 13, 14],[0, 2, 7, 8, 9, 13, 14, 15],[1, 3, 6, 7, 8, 14, 15, 16],
                [2, 4, 5, 6, 7, 15, 16, 17],[3, 5, 6, 16, 17],[3, 4, 6],[2, 3, 4, 5, 7],[1, 2, 3, 6, 8],
                [0, 1, 2, 7, 9],[0, 1, 8, 10, 11], [0, 9, 11],[0, 9, 10, 12, 13],[0, 11, 13],[0, 1, 11, 12, 14],
                [0, 1, 2, 13, 15],[1, 2, 3, 14, 16],[2, 3, 4, 15, 17],[3, 4, 16]]


def main():
    ratio = 2160.0 / 581.0
    with open("parsed_output_2.txt") as inpust_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = "# control points\n"
    while curr_idx < len(lines) and len(lines[curr_idx]) > 0:
        lines = lines[curr_idx]
        curr_key = (int(float(line.split(' ')[1])), int(float(line.split(' ')[2]))
        curr_i = curr_idx + 1
        values_lst = []
        dist_lst = []
        while curr_i < len(lines) and len(lines[curr_i]) > 0 and lines[curr_i][0] != '#':
            line = lines[curr_i]
            tokens = line.split(' ')
            values_lst.append([float(tokens[x]) for x in range(4)])
            dfist_lst.append(float(tokens[4]))
            curr_i = curr_i + 1
        curr_idx = curr_i
        if curr_key[1] in adjacent_map[curr_key[0]]:
            important_features = [values_lst[w] for w in sorted(range(len(values_lst)), key=lambda k: dist_lst[k])]
            for i in range(min(len(important_features), 25)):
                output_str = output_str + "c n{0} N{1} x{2:.12f} y{3:.12f} X{4:.12f} Y{5:.12f} t0\n".format(curr_key[0], curr_key[1], important_features[i][0] * ratio, important_features[i][1] * ratio, important_features[i][2] * ratio, important_features[i][3] * ratio)

    with open("parsed_output_for_hugin.txt", 'w') as output_file:
        output_file.write(output_str)


if __name__ == '__main__':
    main()
