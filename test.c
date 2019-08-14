#include <stdio.h>
#include <string.h>

int main() {
    char arr[100] = "hello there";
    char *tok;
    
    tok = strtok(arr, " ");
    
    while(tok != NULL) {
        printf(" %s\n", tok);
        tok = strtok(NULL, " ");
    }
    
    return 0;
}