#include <ctype.h>
#include <stdio.h>

typedef struct {
    unsigned long long bytes;
    unsigned long long lines;
    unsigned long long words;
    unsigned long long chars;
} FileStats;

int get_file_stats(const char *path, FileStats *stats) {
    FILE *fp = fopen(path, "rb");
    if (fp == NULL) {
        return 0;
    }

    FileStats s = {0, 0, 0, 0};
    int c;
    int prev_space = 1;
    int last_char = '\0';

    while ((c = fgetc(fp)) != EOF) {
        s.chars++;
        s.bytes++;
        last_char = c;

        if (c == '\n') {
            s.lines++;
        }

        if (isspace((unsigned char)c)) {
            prev_space = 1;
        } else if (prev_space) {
            s.words++;
            prev_space = 0;
        }
    }

    if (s.chars > 0 && last_char != '\n') {
        s.lines++;
    }

    fclose(fp);
    if (stats != NULL) {
        *stats = s;
    }
    return 1;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return 1;
    }

    FileStats stats;
    if (!get_file_stats(argv[1], &stats)) {
        perror("fopen");
        return 1;
    }

    printf("bytes: %llu\n", stats.bytes);
    printf("lines: %llu\n", stats.lines);
    printf("words: %llu\n", stats.words);
    printf("chars: %llu\n", stats.chars);

    return 0;
}
