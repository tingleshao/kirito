#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>


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

float ** sort_features(float ** values_lst) {
  float important_features[25][4];
  return *important_features;
}

int contains(int key, int * set) {
    int set_size = sizeof(set) / sizeof(set[0]);

    for (int i = 0; i < set_size; i++) {
       if (key == set[i]) {
         return 1;
       }
    }
   return 0;

}
int main() {
    float ratio = 920.0 / 670.0;

    char const* const filename = "parsed_output.txt";
    FILE* file = fopen(filename, "r");
    char line[256];

    int curr_idx = 0;
    char * output = "# control points\n";

    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
        char ** tokens;
        tokens = str_split(line, ' ');
        int curr_key_0 = atoi(tokens[1]);
        int curr_key_1 = atoi(tokens[2]);
        int curr_key[] = {curr_key_0, curr_key_1};
        int curr_i = curr_idx + 1;

        float values_lst[1000][4];
        int dist_lst[1000];

        while ((strcmp(line, "") != 1) && (line[0] != '#')) {
            values_lst[curr_i][0] = atof(tokens[0]);
            values_lst[curr_i][1] = atof(tokens[1]);
            values_lst[curr_i][2] = atof(tokens[2]);
            values_lst[curr_i][3] = atof(tokens[3]);
            dist_lst[curr_i] = atoi(tokens[4]);
            curr_i++;
        }

        curr_idx = curr_i;
        char * output_str;
        char ** adjacent_map;  // TODO: make this work
        if (contains(curr_key[1], adjacent_map[curr_key[0]])) {
            float ** important_features = sort_features(values_lst);
            for (int i = 0; i < 1000; i++) { //TODO: the upper limit is the min between 25 and the length of the list of features
                char * temp;
                sprintf(temp, "c n%d N%d x%f y%f X%f Y%f t0\n",
                    curr_key[0], curr_key[1], important_features[i][0] * ratio,
                    important_features[i][1] * ratio, important_features[i][2] * ratio,
                    important_features[i][3] * ratio);
                output = strcat(output, temp);
            }
        }
    }
    printf(output);
    return 0;
}
