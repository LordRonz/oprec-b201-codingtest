#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    char s[100];
    int t = 0;
    scanf("%s", s);
    for(int i = 0; s[i]; ++i) {
        t += s[i] - '0';
    }
    puts(t % 3 == 0 && s[strlen(s) - 1] % 2 == 0 ? "SUS" : "NOT SUS");
}
