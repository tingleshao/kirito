from sys import argv
# convert the opencv output into some plain text format, which is easier to be
#   passed into later stages


def main():
    with open(argv[1]) as opencv_output:
        text = opencv_output.read()
    lines = text.split('\n')
    output = ""
    for line in lines:
        tokens = line.split(" ")
        if line[0:22] == 'pairwise_matches index':
            src_img_idx = int(tokens[4].split(":")[1])
            dst_img_idx = int(tokens[7].split(":")[1])
            if not (src_img_idx == -1) and not (dst_img_idx == -1):
                output = output + "# {} {}\n".format(src_img_idx, dst_img_idx)
        elif line[0:7] == 'matches':
            query_id = int(tokens[5])
            query_x = float(tokens[9])
            query_y = float(tokens[10])
            train_id = int(tokens[13])
            train_x = float(tokens[17])
            train_y = float(tokens[18])
            distance = float(tokens[20])
            output = output + "{0} {1} {2} {3} {4} {5} {6}\n".format(query_x, query_y, train_x, train_y, distance, query_id, train_id)
    with open("parsed_output.txt", "w") as text_file:
        text_file.write(output)


if __name__ == '__main__':
    main()
