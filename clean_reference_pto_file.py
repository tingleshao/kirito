# clean referenc pto file:
# remove all the control points
import sys


def clean_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ""
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if len(line) > 0 and (line[0] == "v" or line[0] == "c"):
            output_str = output_str + ""
        elif len(line) > 0 and line == "# specify variables that should be optimized":
            output_str = output_str + line + "\n" + "v" + "\n"
        else:
            output_str = output_str + line + "\n"
        curr_idx = curr_idx + 1
    with open(filename, 'w') as output_file:
        output_file.write(output_str)


if __name__ == "__main__":
    clean_file(sys.argv[1])
