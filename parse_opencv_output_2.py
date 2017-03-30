from sys import argv


# convert the opencv output into some plain text format, which is easier to be
#   passed into later stages

def main():
    with opencv(argv[1]) as opencv_output:
        text = opencv_output.read()
    lines = text.split('\n')
    output = ""
    for line in lines:
        tokens = line.split(" ")
        if line[0:22] == 'pairwise_matches index':
            src_img_idx = int(tokens[4].split(":")[1])
            dst_img_idx = int(tokens[7].split(":")[1])
            if not (src_img_idx == -1) and not (dst_img_idx == -1):
                # TODO; here replace 0 with @
                output = output + "# {} {}\n".format(src_img_idx, dst_img_idx)
            elif line[0:7] == 'matches':
                query_x = float(tokens[9])
                query_y = float(tokens[10])
                train_x = float(tokens[17])
                train_y = float(tokens[18])
                distance = float(tokens[20])
                output = output + "{0} {1} {2} {3} {4}\n".format(query_x, query_y, train_x, train_y, distance)
    with open("parsed_output.txt", "w") as text_file:
        text_file.write(output)


if __name__ == '__main__':
    main()
