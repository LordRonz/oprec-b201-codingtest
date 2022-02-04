#include <cstdio>

using namespace std;

int main() {
	int xcnt = 0, res = 0;
	char s[350];
	scanf("%s", s);
	for(int i = 0; s[i]; ++i) {
		if(s[i] == 'x') {
			++xcnt;
		}
		else {
			xcnt = 0;
		}
		if(xcnt > 2) ++res;
	}
	printf("%d\n", res);
}