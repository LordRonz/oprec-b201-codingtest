from random import choice, randint, shuffle
from typing import Dict
t = 30

def gen_char():
    return choice('abcdefghijklmnopqrstuvwxyz')

def gen_name(n: int):
    return ''.join(gen_char() for _ in range(n))

def generate_testcase(ith = 1):
    n = randint(1, 100069)
    n1 = randint(1, n)
    n2 = n - n1

    s = [[1, gen_name(randint(3, 169))] for _ in range(n1)]
    for _ in range(n2):
        s[randint(0, n1 - 1)][0] += 1

    s2 = [item for l in [[a[1] for _ in range(a[0])] for a in s] for item in l]
    shuffle(s2)

    q = '\n'.join(s2)

    h: Dict = {}

    a = []
    for c in s2:
        if c in h:
            h[c] += 1
            temp = c + str(h[c])
            a.append(temp)
        else:
            h[c] = 0
            a.append('OK')

    ans = '\n'.join(a)

    with open(f'{ith}.in', 'w') as f:
        f.write(f'{n}\n' + q + '\n')

    with open(f'{ith}.out', 'w') as f:
        f.write(ans + '\n')

for i in range(t):
    generate_testcase(i + 1)
