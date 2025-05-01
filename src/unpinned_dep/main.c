#include <stdio.h>

#include "lib_unpinned.h"

void main(int argc, char **argv) {
    printf("Calling a library function...\n");
    library_fn();
    printf("Complete.\n");
}