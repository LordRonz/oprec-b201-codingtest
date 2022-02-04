from random import choice, randint
t = 10

def gen_rand_str():
    return choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def generate_testcase(ith = 1):
    n = randint(1, 69)
    s = ''.join(gen_rand_str() for _ in range(n))

    with open(f'{ith}.in', 'w') as f:
        f.write(s + '\n')

    with open(f'{ith}.out', 'w') as f:
        f.write(s + '\n')

for i in range(t):
    generate_testcase(i + 1)
