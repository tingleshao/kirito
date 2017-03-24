
# Make it:
# for every image pair, we examine if the matched features are between the 30%, if not then we remove it.
#

relations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
img_size = [1033, 581]

relations_map = {"0#1": w, "0#11": , "0#9": , "":, "":, "":, "":, "":, "":, "":, "":, "":, "":,
                 "":, "":, "":, "":, "":, "":, "":, "":,
                 "":, "":, "":, "":, "":, "":, "":, "":,
                 "":, "":, "":, "":, "":, "":, "":, "":,
                 "":, "":, "":, "":, "":, "":, "":, "":,
                 "":, "":, "":, "":, "":, "":, "":, "":,
                 "":, "":, "":, "":, "":, "":, "":, "":,
                 "":, "":, "":, "":, "":, "":, "":, "":, }

                 
def is_good_match(match, percent, relation, img_size):
    # match format: [x1, y1, x2, y2]
    # percent: (p1, p2) the percentage of overlapping in the images
    # relation: the second image relate to the first one, e: 0, w: 1, n: 2, s: 3
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
    return False


def main():
    return None
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
        output_str = output_str + line + "\n"
        while curr_i < len(lines) and len(lines[curr_i]) > 0 and lines[curr_i][0] != '#':
            line = lines[curr_i]
            tokens = line.split(' ')
            match = [float(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3])]
            percent = [0.3, 0.3]
            relation = 0
            if is_good_match(match, percent, relation, img_size):
                output_str = output_str + line + "\n"
    with open("parsed_output_2.txt", 'w') as output_file:
        output_file.wrfite(output_str)

if __name__ == '__main__':
    main()
