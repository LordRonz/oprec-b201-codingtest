#include <cstdio>

int main() {
    int a, odd = 0, even = 0, ans = 0, n;
    scanf("%d", &n);
    for(int i = 0; i < n; ++i) {
        scanf("%d", &a);
        if(a & 1) {
            ++odd;
        } else {
            ++even;
        }
        if((odd > 1 && even == 1) || (even > 1 && odd == 1)) {
            ans = i;
            break;
        }
    }
    printf("%d\n", ans);
}