#include <stdio.h>
#include <string.h>

int main() {
    char s[200];
    int x;
    scanf("%s", s);
    x = s[strlen(s) - 1] - '0';
    puts(x & 1 ? "SUS" : "NOT SUS");
}