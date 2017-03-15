import os

idx_map = [13, 14, 15, 16, 17, 18, 12, 1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6]
for i in range(18):
    for j in range(3):
        os.system("cp ../frame_0_copy/mcam_{0}_scale_{1}.jpg mcam_{2}_scale_{3}.jpg".format(i+1, j, idx_map[i], j))
