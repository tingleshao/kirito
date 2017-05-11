# update the resolution in a pto file.


def main():
    with open("optimized.pto") as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ''
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if len(line) > 0 and line[0] == "p":
            tokens = line.split(" ")
            width = int(tokens[2][1:])
            height = int(tokens[3][1:])
            new_width = str(width / 10)
            new_height = str(height / 10)
            new_line = "p " + tokens[1] + " w" + new_width + " h" + new_height + " " + " ".join(tokens[4:])
            output_str = output_str + new_line + "\n"
        else:
            output_str = output_str + line + "\n"
        curr_idx = curr_idx + 1
    with open("optimized_s.pto", 'w') as output_file:
        output_file.write(output_str)


if __name__ == '__main__':
    main()
