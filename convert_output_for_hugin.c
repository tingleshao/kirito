#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>


// TODO: implement the samething as the one in parse_output_for_hugin.py
char** str_split(char* a_str, const char a_delim) {
    char** result    = 0;
    size_t count     = 0;
    char* tmp        = a_str;
    char* last_comma = 0;
    char delim[2];
    delim[0] = a_delim;
    delim[1] = 0;

    /* Count how many elements will be extracted. */
    while (*tmp) {
        if (a_delim == *tmp) {
            count++;
            last_comma = tmp;
        }
        tmp++;
    }

    /* Add space for trailing token. */
    count += last_comma < (a_str + strlen(a_str) - 1);

    /* Add space for terminating null string so caller
       knows where the list of returned strings ends. */
    count++;

    result = malloc(sizeof(char*) * count);

    if (result) {
        size_t idx  = 0;
        char* token = strtok(a_str, delim);

        while (token) {
            assert(idx < count);
            *(result + idx++) = strdup(token);
            token = strtok(0, delim);
        }
        assert(idx == count - 1);
        *(result + idx) = 0;
    }
    return result;
}


void main() {
// TODO: implement me
    float ratio = 920.0 / 670.0;

    char const* const filename = "parsed_output.txt";
    FILE* file = fopen(filename, "r");
    char line[256];
    char *output;

    int curr_idx = 0;
    char * output = "# control points\n";

    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
        char ** tokens;
        tokens = str_split(line, " ");
        int curr_key_0 = atoi(tokens[1]);
        int curr_key_1 = atoi(tokens[2]);
        int curr_i = curr_idx + 1;

        while (curr_i < xxx) && (len(line) > 0) && (line[0] != "#") {
            values_lst.append([float(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3])]);
            dist_lst.append(int(tokens[4]));
            curr_i ++;
        }
        curr_idx = curr_i;
        if (curr_key[1] in adjacent_map[curr_key[0]]) {
            important_features = sort ...
            for (int i = 0; i < xx; i++) { //TODO: the upper limit is the min between 25 and the length of the list of features
                output_str = output_str + "c n%d N%d x%f y%f X%f Y%f t0\n", curr_keyp[0], curr_key[1], important_features[i][0] * ratio, important_features[i][1] * ratio, important_features[i][2] * ratio, important_features[i][3] * ratio;
            }
        }
     // TODO: save the output into text file
    }
}
