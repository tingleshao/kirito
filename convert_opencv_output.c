// TODO: write the samething in C as parse_opencv_output.py

#include <stdio.h>



int main(int argc, char **argv) {
    // TODO: implement me
    for (int i = 0; i < argc; ++i) {
        printf("argv[%d]: %s\n", i, argv[i]);
    }

    // TODO: read input
    char const* const filename = argv[1];
    FILE* file = fopen(filename, "r");
    char line[256];

    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }
    fclose(file);
    return 0;
}
