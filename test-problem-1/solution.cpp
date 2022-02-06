#include <cstdio>

using namespace std;

int main() {
    int a[105], odd = 0, even = 0, ans = 0, n;
    scanf("%d", &n);
    for(int i = 0; i < n; ++i) {
        scanf("%d", a + i);
        a[i] & 1 ? ++odd : ++even;
    }
    for(int i = 0; i < n; ++i) {
        if((a[i] & 1) == (odd == 1 ? 1 : 0)) {
            ans = i;
            break;
        }
    }
    printf("%d\n", ans);
}