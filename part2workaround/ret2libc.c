#include <errno.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv){
    FILE *f;
    long filelen;
    unsigned char *buffer;
    char * new_arg[3] = {NULL};

    if(argc != 3)
        exit(1);

    new_arg[0] = argv[1];

    f = fopen(argv[2], "rb");
    fseek(f, 0, SEEK_END);
    filelen = ftell(f);

    buffer = malloc(filelen);
    fseek(f, 0, SEEK_SET);
    fread(buffer, 1, filelen, f);
    fclose(f);
    new_arg[1] = buffer;
    if(execvp(argv[1], new_arg) == -1)
            printf("execve error: %s\n", strerror(errno));
    return 1;
}
