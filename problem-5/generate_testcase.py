from random import randint, choice

t = 30

def gen_num(yes = True):
    return randint(1, 6999999999999999999999999999999999999999999696969) if not yes else randint(1, 999999999999999999999999999999999999999999696969) * 6

def generate_testcase(ith = 1):
    yes = choice((True, False))
    num = gen_num(yes)

    ans = 'SUS' if num % 6 == 0 else 'NOT SUS'

    with open(f'testcase/{ith}.in', 'w') as f:
        f.write(f'{num}\n')

    with open(f'testcase/{ith}.out', 'w') as f:
        f.write(ans + '\n')

for i in range(t):
    generate_testcase(i + 1)
