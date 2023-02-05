from random import choice, randint, shuffle
t = 20

def gen_num(i):
    return f'{randint(0 if i != 0 else 1, 9)}'

def generate_testcase(ith = 1):
    n = randint(1, 169)
    s = ''.join(gen_num(a) for a in range(n))
    x = int(s[-1])
    ans = 'SUS' if x & 1 else 'NOT SUS'

    with open(f'testcase_sharif/in/input{ith}.txt', 'w') as f:
        f.write(s + '\n')

    with open(f'testcase_sharif/out/output{ith}.txt', 'w') as f:
        f.write(ans + '\n')

for i in range(t):
    generate_testcase(i + 1)
