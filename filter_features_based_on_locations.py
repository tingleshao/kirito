# For every image pair, we examine if the matched features are inside the overlaopping regions, if not then we remove it.


img_size = [1033, 581]

relations_map = {"0#1": 1, "0#9":2, "0#11":0, "0#13":3, "1#2":1, "1#8":2, "1#14":3,
                 "2#3":1, "2#7":2, "2#15":3, "3#4":1, "3#6":2, "3#16":3,
                 "4#5":2, "4#17":3, "5#6":0, "6#7":0, "7#8":0, "8#9":0, "9#10":0, "10#11":3,
                 "11#12":3, "12#13":1, "13#14":1, "14#15":1, "15#16":1, "16#17":1,
                 "0#8":5, "0#10":4, "0#12":6, "0#14":7, "1#7":5, "1#9":4, "1#13":6,
                 "1#15":7, "2#6":5, "2#8":4, "2#14":6, "2#16":7, "3#5":5,
                 "3#7":4, "3#15":6, "3#17":7, "9#11":6, "11#13":7}


def is_good_match(match, percent, relation, img_size):
    # match format: [x1, y1x2, y2]
    # percent: (p1, p2) the percentage of overlapping in the images
    # relation: the second image relate to the first one,
    # e: 0, w: 1, n: 2, s: 3, ne: 4, nw: 5, se: 6, sw: 7
    # image size: the size of each image
    if relation == 0:
        # the second image is right to the first image
        if match[0] > ((1.0 - percent[0]) * img_size[0]) and match[2] < (percent[1] * img_size[0]):
            return True
    elif relation == 1:
        # the second image is left to the first image
        if match[0] < (percent[0] * img_size[0]) and match[2] > ((1.0 - percent[1]) * img_size[0]):
            return True
    elif relation == 2:
        # the second image is top to the first image
        if match[1] < (percent[0] * img_size[1]) and match[3] > ((1.0 - percent[1]) * img_size[1]):
            return True
    elif relation == 3:
        # the second image is down to the first image
        if match[1] > ((1.0 - percent[0]) * img_size[1]) and match[3] < (percent[1] * img_size[1]):
            return True
    elif relation == 4:
        # the second image is top right to the first image
        if match[0] > ((1.0 - percent[0]) * img_size[0]) and match[2] < (percent[1] * img_size[0]) and \
           match[1] < (percent[0] * img_size[1]) and match[3] > ((1.0 - percent[1]) * img_size[1]):
           return True
    elif relation == 5:
        # the second image is top left to the first image
        if match[0] < (percent[0] * img_size[0]) and match[2] > ((1.0 - percent[1]) * img_size[0]) and \
           match[1] < (percent[0] * img_size[1]) and match[3] > ((1.0 - percent[1]) * img_size[1]):
           return True
    elif relation == 6:
        # the second image is down right to the first image
        if match[0] > ((1.0 - percent[0]) * img_size[0]) and match[2] < (percent[1] * img_size[0]) and \
           match[1] > ((1.0 - percent[0]) * img_size[1]) and match[3] < (percent[1] * img_size[1]):
           return True
    elif relation == 7:
        # the second image is down left to the first image
        if match[0] < (percent[0] * img_size[0]) and match[2] > ((1.0 - percent[1]) * img_size[0]) and \
           match[1] > ((1.0 - percent[0]) * img_size[1]) and match[3] < (percent[1] * img_size[1]):
           return True
    return False


def main():
    with open("parsed_output.txt") as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ''
    while curr_idx < len(lines) and len(lines[curr_idx]) > 0:
        line = lines[curr_idx]
        curr_key = (int(float(line.split(' ')[1])), int(float(line.split(' ')[2])))
        curr_i = curr_idx + 1
        values_lst = []
        dist_lst = []
        output_str = output_str + line + "\n"
        while curr_i < len(lines) and len(lines[curr_i]) > 0 and lines[curr_i][0] != '#':
            line = lines[curr_i]
            tokens = line.split(' ')
            match = [float(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3])]
            percent = [0.20, 0.24]
            key = str(curr_key[0]) + "#" + str(curr_key[1])
            reverse_key = str(curr_key[1]) + "#" + str(curr_key[0])
            if key in relations_map: # has_key() was removed in Python 3
                relation = relations_map[key]
                if is_good_match(match, percent, relation, img_size):
                    output_str = output_str + line + "\n"
            # test inverse relation
            elif reverse_key in relations_map:
                relation = relations_map[reverse_key]
                reverse_match = [match[2], match[3], match[0], match[1]]
                if is_good_match(reverse_match, percent, relation, img_size):
                    output_str = output_str + line + "\n"
            else:
                print("no such relation: " + key)
            curr_i = curr_i + 1
        curr_idx = curr_i

    with open("parsed_output_2.txt", 'w') as output_file:
        output_file.write(output_str)


if __name__ == '__main__':
    main()
