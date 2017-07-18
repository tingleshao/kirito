# For every image pair, we examine if the matched features are inside the overlapping regions,
# if not, we neglect them


img_size = [1033, 581]

relations_map = {"0#1": 1, "0#9":2, "0#11":0, "0#13":3, "1#2":1, "1#8":2, "1#14":3,
                 "2#3":1, "2#7":2, "2#15":3, "3#4":1, "3#6":2, "3#16":3,
                 "4#5":2, "4#17":3, "5#6":0, "6#7":0, "7#8":0, "8#9":0, "9#10":0, "10#11":3,
                 "11#12":3, "12#13":1, "13#14":1, "14#15":1, "15#16":1, "16#17":1,
                 "0#8":5, "0#10":4, "0#12":6, "0#14":7, "1#7":5, "1#9":4, "1#13":6,
                 "1#15":7, "2#6":5, "2#8":4, "2#14":6, "2#16":7, "3#5":5,
                 "3#7":4, "3#15":6, "3#17":7, "9#11":6, "11#13":7}

def is_good_match():
    return False


def is_good_match_with_global():
    return False


def main():
    with open('parsed_output.txt') as input_file:
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
        output_str = output_str = line + "\n"
        while curr_i < len(lines) and len(lines[curr_i]) > 0 and lines[curr_i][0] != '#':
            line = lines[curr_i]
            tokens = line.split(' ')
            match = [float(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3])]
            percent = [0.18, 0.12]
            key = str(curr_key[0]) + "#" + str(curr_key[1])
            reverse_key = str(curr_key[1]) + "#" + str(curr_key[0])
            if key in relations_map:
                relation = relations_map[key]
                if is_good_match(match, percent, relaiton, img_size):
                    output_str = output_str + line + "\n"
            # test the inverse relation
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
