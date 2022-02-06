from random import randint
from typing import Deque, Set
from collections import deque

t = 30

def generate_testcase(ith = 1):
    n, m = randint(1, 100069), randint(1, 100069)

    look: Set[int] = set()

    d: Deque[list[int]] = deque()

    ans = 0

    if n > m:
        ans = n - m
    else:
        d.append([n, 0])
        look.add(n)
        while d:
            a = d[0][0]
            step = d[0][1]
            d.popleft()
            if a == m:
                ans = step
                break
            if a <= 0:
                continue
            if a - 1 > 0 and (a - 1) not in look:
                d.append([a - 1, step + 1])
                look.add(a - 1)
            if a * 2 < m * 2 and (a * 2) not in look:
                d.append([a * 2, step + 1])
                look.add(a * 2)

    with open(f'testcase/{ith}.in', 'w') as f:
        f.write(f'{n} {m}\n')

    with open(f'testcase/{ith}.out', 'w') as f:
        f.write(f'{ans}\n')

for i in range(t):
    generate_testcase(i + 1)
