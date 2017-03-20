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

float ** sort_features(float ** values_lst, int * dist_lst, int length) {
  // TODO: implement me
  float important_features[25][4];

  //  sort dist lst
  // dumb sort
  for (int i = 0; i < length; i++) {
      for (int j = 0; j < length-1; j++) {
          if (dist_lst[j] > dist_lst[j+1]) {
              int temp = dist_lst[j];
              dist_lst[j] = dist_lst[j+1];
              dist_lst[j+1] = temp;
          }
      }
  }

  // fill in important features
  for (int i = 0; i < 25; i++) {
    important_features[i][0] = values_lst[dist_lst[i]][0];
    important_features[i][1] = values_lst[dist_lst[i]][1];
    important_features[i][2] = values_lst[dist_lst[i]][2];
    important_features[i][3] = values_lst[dist_lst[i]][3];
  }

  return important_features;
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

int sizeof_arr(int * arr) {
    int size = sizeof(arr) / sizeof(arr[0]);
    return size;
}

int min(int a, int b) {
  if (a > b) {
    return b;
  }
  return a;
}

int main() {
    float ratio = 920.0 / 670.0;

    char const* const filename = "parsed_output.txt";
    FILE* file = fopen(filename, "r");
    char line[256];

    int curr_idx = 0;
    char * output = "# control points\n";

    float values_lst[2000][4];
    int dist_lst[2000];
    int first_line = 1;
    int curr_i;

    int adjacent_map[18][3] = {{1, 11, -1}, {0, 2, -1}, {1, 3, -1}, {2, 4, -1},
        {5, -1, -1}, {4, 6, -1}, {5, 7, -1}, {6, 8, -1}, {7, 9, -1}, {8, 10, -1},
        {9, 11, -1}, {0, 10, 12}, {11, 13, -1}, {12, 14, -1}, {13, 15, -1},
        {14, 16, -1}, {15, 17, -1}, {4, 16, -1}};

    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
        char ** tokens;
        tokens = str_split(line, ' ');
        int curr_key_0;
        int curr_key_1;
        int curr_key[2];

        if ((strcmp(line, "") != 1) && ((line[0]) == '#')) { // header line
            curr_key[0] = atoi(tokens[1]);
            curr_key[1] = atoi(tokens[2]);
            if (!first_line) {
                float ** important_features = sort_features(values_lst, dist_lst, curr_i);
                for (int i = 0; i < min(25, sizeof_arr(important_features)); i++) {
                    char * temp;
                    sprintf(temp, "c n%d N%d x%f y%f X%f Y%f t0\n",
                        curr_key[0], curr_key[1], important_features[i][0] * ratio,
                        important_features[i][1] * ratio, important_features[i][2] * ratio,
                        important_features[i][3] * ratio);
                    output = strcat(output, temp);
                }
            }
            curr_i = 0;
            first_line = 0;
        }
        else if ((strcmp(line, "") != 1) && ((line[0]) != '#')) {
            values_lst[curr_i][0] = atof(tokens[0]);
            values_lst[curr_i][1] = atof(tokens[1]);
            values_lst[curr_i][2] = atof(tokens[2]);
            values_lst[curr_i][3] = atof(tokens[3]);
            dist_lst[curr_i] = atoi(tokens[4]);
            curr_i++;
        }
    }
    printf("%s", output);
    return 0;
}
