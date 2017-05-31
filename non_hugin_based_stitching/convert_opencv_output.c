// TODO: write the samething in C as parse_opencv_output.py

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


int main(int argc, char **argv) {
    for (int i = 0; i < argc; ++i) {
        printf("argv[%d]: %s\n", i, argv[i]);
    }

    char const* const filename = argv[1];
    FILE* file = fopen(filename, "r");
    char line[256];

    char *output;

    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
        char *start = &line[0];
        char *end = &line[22];
        char *substr = (char *)calloc(1, end-start+1);
        memcpy(substr, start, end-start);
        printf("%s\n", substr);
        char *end2 = &line[7];
        char *substr2 = (char *)calloc(1, end2-start+1);
        memcpy(substr2, start, end2-start);
        printf("%s\n", substr2);
        // head of a group of matches
        if (strcmp(substr, "pairwise_matches index") != 0) {
            char **tokens;
            const char delim = ' ';
            tokens = str_split(line, delim);

            int src_img_idx = atoi(str_split(tokens[4], ':')[1]);
            int dst_img_idx = atoi(str_split(tokens[7], ':')[1]);
            if ((src_img_idx != -1) && (dst_img_idx != -1)) {
                char *temp;
                sprintf(temp, "# %d %d\n", src_img_idx, dst_img_idx);
                output = strcat(output, temp);
            }
        }
        else if (strcmp(substr2, "matches")) {
            char **tokens;
            tokens = str_split(line, ' ');
            float query_x = atof(tokens[9]);
            float query_y = atof(tokens[10]);
            float train_x = atof(tokens[17]);
            float train_y = atof(tokens[18]);
            int distance = atoi(tokens[20]);
            char *temp;
            sprintf(temp, "%f %f %f %f %d\n", query_x, query_y, train_x, train_y, distance);
            output = strcat(output, temp);
        }
    }
    fclose(file);
    return 0;
    //TODO:  save the variable output to a text file
}
