#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int calc(int n) {
    if ((n == 1) || (n == 2)) {
        return n;    
    } else {
        return calc(n - 1) + calc(n - 2);
    }
}

int main() {
    char line[80];
    int n;
    printf("How many steps are there in the staircase?: ");
    fgets(line, 80, stdin);
    n = atoi(line);
    printf("Testing for %i steps...\n", n);
    printf("There are %i ways!\n", calc(n));
}
