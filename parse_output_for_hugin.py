import math


# we need to scale the feature location numbers because
# the opencv feature extraction is based on scale image
# in resolution 670 x 895
# while hugen takes in original image resolution
# 920 x 1228
keymap = [12, 13, 14, 15, 16, 17, 11, 0, 1, 2, 3, 4, 10, 9, 8, 7, 6, 5]

def main():
    ratio = 920.0 / 670.0
    with open('parse_output.txt') as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = '# control points\n'
    while curr_idx < len(lines) and len(lines[curr_idx]) > 0:
        line = lines[curr_idx]
        curr_key = (int(float(line.split(' ')[1])), int(float(line.split(' ')[2])))
        curr_i = curr_idx + 1
        values_lst = []
        dist_lst = []
        while curr_i < len(lines) and len(lines[curr_i]) > 0 and lines[curr_i][0] != '#':
            line = lines[curr_i]
            tokens = line.split(' ')
            values_lst.append([float(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3])])
            dist_lst.append(int(tokens[4]))
            curr_i = curr_i + 1
        curr_idx = curr_i
#        print("curr_idx: " + str(curr_idx))
#        print("currline for curridx: " + lines[curr_idx])
    #    print(sorted(range(len(values_lst)), key=lambda k: dist_lst[k]))
        important_features = [values_lst[w] for w in sorted(range(len(values_lst)), key=lambda k: dist_lst[k])]
        for i in range(min(len(important_features), 25)):
            output_str = output_str + "c n{0} N{1} x{2:.12f} y{3:.12f} X{4:.12f} Y{5:.12f} t0\n".format(keymap[curr_key[0]], keymap[curr_key[1]], important_features[i][0] * ratio, important_features[i][1] * ratio, important_features[i][2] * ratio, important_features[i][3] * ratio)
    with open("parsed_output_for_hugin.txt", "w") as text_file:
        text_file.write(output_str)


if __name__ == '__main__':
    main()
