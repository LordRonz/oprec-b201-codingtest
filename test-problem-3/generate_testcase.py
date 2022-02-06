from random import choice, randint, shuffle

t = 20

def gen_char():
    return choice('abcdefghijklmnopqrstuvwxyz')

def generate_testcase(ith = 1):
    n = randint(3, 169)
    nx = randint(0, 169)

    l = list(''.join(gen_char() for _ in range(n)) + ('x' * nx))
    shuffle(l)
    s = ''.join(l)

    x, ans = 0, 0
    for c in s:
        if c == 'x':
            x += 1
            if x > 2:
                ans += 1
        else:
            x = 0

    with open(f'testcase/{ith}.in', 'w') as f:
        f.write(s + '\n')

    with open(f'testcase/{ith}.out', 'w') as f:
        f.write(f'{ans}\n')

for i in range(t):
    generate_testcase(i + 1)
