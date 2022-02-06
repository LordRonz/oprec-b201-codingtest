#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    char s[400];
    int a = 0, b, diff = 0;
    bool pal = true;
    scanf("%s", s);
    b = strlen(s) - 1;
    while(a < b) {
        if(s[a++] != s[b--]) {
            pal = false;
            ++diff;
        }
    }
    puts(pal ? "kasur nababan rusak" : "anta baka");
    if(!pal) {
        printf("%d\n", diff);
    }
}
