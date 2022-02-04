#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    char s[400];
    int a = 0, b;
    bool pal = true;
    scanf("%s", s);
    b = strlen(s) - 1;
    while(a < b) {
        if(s[a++] != s[b--]) {
            pal = false;
            break;
        }
    }
    puts(pal ? "kasur nababan rusak" : "anta baka");
}
