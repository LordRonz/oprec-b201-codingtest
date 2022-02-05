#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    char s[200];
    int n, a, f = 0, g, l;
    scanf("%d", &n);
    for(int i = 0; i < n; ++i) {
        scanf("%d", &a);
        f += i & 1 ? -a : a;
    }
    scanf("%s", s);
    l = strlen(s);
    g = (f < 0 ? -f : f) % l;
    g = f < 0 ? l - g : g;
    for(int i = l - g; i < l; ++i) {
        printf("%c", s[i]);
    }
    for(int i = 0; i < l - g; ++i) {
        printf("%c", s[i]);
    }
    puts("");
}
