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
    updated_v = False
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if line == "#-hugin  cropFactor=1":
            output_str  = output_str + "#-hugin  cropFactor=7" + '\n'
        elif not updated_v and len(line) > 20 and line[0:20] == "i w3840 h2160 f0 v50":
            output_str = output_str + "i w3840 h2160 f0 v12.299017381458" + line[20:] + '\n'
            updated_v = True
        elif len(line) > 20 and line[-9:-1] == "418.jpeg":
            output_str = output_str + "i w3840 h2160 f0 v75.1633550117801 Ra0 Rb0 Rc0 Rd0 Re0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a0 b0 c0 d0 e0 g0 t0 Va1 Vb0 Vc0 Vd0 Vx0 Vy0  Vm5 n\"418.jpeg\"" + '\n'
        else:
            output_str = output_str + line + '\n'
        curr_idx = curr_idx + 1
    with open("init2.pto", 'w') as output_file:
        output_file.write(output_str)


if __name__ == "__main__":
    main()
