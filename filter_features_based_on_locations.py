# TODO: implement this: filter features based on locaitons

# Make it:
# for every image pair, we examine if the matched features are between the 30%, if not then we remove it.
#

def is_good_match(match, percent, relation):
    # match format: [x1, y1, x2, y2]
    # percent: (p1, p2) the percentage of overlapping in the images
    # relation: the second image relate to the first one, e: 0, w: 1, n: 2, s: 3
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
            if is_good_match(match):
                output_str = output_str + line + "\n"
    with open("parsed_output_2.txt", 'w') as output_file:
        output_file.wrfite(output_str)

if __name__ == '__main__':
    main()
