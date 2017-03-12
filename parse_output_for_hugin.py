


def main():
    with open('parse_output.txt') as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    line = lines[curr_idx]
    while curr_idx < len(lines):
        curr_key = (int(line[0].split(' ')[1]), int(line[0].split(' ')[2])
        curr_i = 1
        values_lst = []
        dist_lst = []
        output_str = '# control points\n'
        while lines[curr_i][0] != '#' and curr_i < len(lines):
            line = lines[curr_i]
            tokens = line.split(' ')
            values_lst.append([float(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3])])
            dist_lst.append(int(tokens[4]))
            curr_i = curr_i + 1
        curr_idx = curr_i
        important_features = values_lst[sorted(range(len(values_lst)), key=lambda k: dist_lst[k])]
        for i in range(min(len(important_features), 25)):
            output_str = output_str + "c n{0} N{1} x{2:.12f} y{3:.12f} X{4:.12f} Y{5:.12f} t0\n".format(curr_key.[0], curr_key[1], important_features[i][0], important_features[i][1], important_features[i][2], important_features[i][3])
    with open("parsed_output_for_hugin.txt", "w") as text_file:
        text_file.write(output_str)


if __name__ == '__main__':
    main()
