#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>

extern char **environ;

void library_fn(void) {
    printf("I am a good function.\n");
}