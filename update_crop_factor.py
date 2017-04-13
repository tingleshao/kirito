# change the crop factor in a pto file.
#
import sys

def main():
    filename = sys.argv[1]
    with open(filename) as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ""
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if line == "#-hugin  cropFactor=1":
            output_str  = output_str + "#-hugin  cropFactor=7" + '\n'
        else:
            output_str = output_str + line + '\n'
    with open("init2.pto", 'w') as output_file:
        output_file.write(output_str)
    

if __name__ == "__main__":
    main()
