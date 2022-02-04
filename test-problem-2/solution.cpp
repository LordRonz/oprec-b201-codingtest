#include <cstdio>

int main() {
    char s[200];
    int low = 0, hi = 0;
    scanf("%s", s);
    for(int i = 0; s[i]; ++i) {
        if(s[i] > 'Z') {
            ++low;
        } else {
            ++hi;
        }
    }
    if(hi > low) {
        puts("HI");
    } else if(hi < low) {
        puts("LOW");
    } else {
        puts("SAME");
    }
}