# Filter out founded matching features based on the matching with global view
# Approach:
#  For any matched features between two images id from 1-18
#      find if the feature indices also exist in the global view matching list
#      if so, keep it. Otherwise discard it.

# build a global view feature matching map:
#  {other_img_id: {other_img_feature_id: [global_img_feature_id, distance]}}

# if in the other img, one other_img_feature has multiple matches in the global
#   img, choose the one with smallest distance



def main():
    # build the map
    global_img_matching_map = {}
    with open("parsed_output.txt") as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ''
    while curr_idx < len(lines) and len(lines[curr_idx]) > 0:
        line = lines[curr_idx]
        curr_key = (int(float(line.split(' ')[1])), int(float(line.split(' ')[2])))
        curr_i = curr_idx + 1
        if curr_key[0] == 0:
            # first image is global view
            while curr_i < len(lines) and len(lines[curr_i]) > 0 and lines[curr_i][0] != '#':
                line = lines[curr_i]
                tokens = line.split(' ')
                other_img_feature_id = int(tokens[6])
                global_img_feature_id = int(tokens[5])
                curr_distance = float(tokens[4])
                if other_img_feature_id in global_img_matching_map[curr_key[1]]:
                    existing_distance = global_img_matching_map[curr_key[1]][other_img_feature_id][1]
                    if existing_distance > curr_distance:
                        global_img_matching_map[curr_key[1]][other_img_feature_id] = [global_img_feature_id, curr_distance]
                else:
                    global_img_matching_map[curr_key[1]][other_img_feature_id] = [global_img_feature_id, curr_distance]
                curr_i = curr_i + 1
        elif curr_key[1] == 0:
            # second image is global view
            while curr_i < len(lines) and len(lines[curr_i]) > 0 and lines[curr_i][0] != '#':
                line = lines[curr_i]
                tokens = line.split(' ')
                other_img_feature_id = int(tokens[5])
                global_img_feature_id = int(tokens[6])
                curr_distance = float(tokens[4])
                if other_img_feature_id in global_img_matching_map[curr_key[0]]:
                    existing_distance = global_img_matching_map[curr_key[1]][other_img_feature_id][1]
                    if existing_distance > curr_distance:
                        global_img_matching_map[curr_key[0]][other_img_feature_id] = [global_img_feature_id, curr_distance]
                else:
                    global_img_matching_map[curr_key[0]][other_img_feature_id] = [global_img_feature_id, curr_distance]
                curr_i = curr_i + 1
        curr_idx = curr_i

        # filter out matches
    with open("parsed_output.txt") as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ''
    while curr_idx < len(lines) and len(lines[curr_idx]) > 0:
        line = lines[curr_idx]
        # only do when image index is not 0
        curr_key = (int(float(line.split(' ')[1])), int(float(line.split(' ')[2])))
        curr_i = curr_idx + 1
        values_lst = []
        dist_lst = []
        if 0 in curr_key:
        else: 
            output_str = output_str = line + "\n"
