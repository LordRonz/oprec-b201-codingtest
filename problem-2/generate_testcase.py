from random import choice, randint
t = 30

def gen_char():
    return choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def gen_word(n: int):
    return ''.join(gen_char() for _ in range(n))

def generate_testcase(ith = 1):
    n1 = randint(3, 169)
    n2 = randint(3, 169)

    d = [randint(3, 169) for _ in range(n1)]
    ds = ' '.join(f'{c}' for c in d)
    s = gen_word(n2)

    f = 0
    for i, a in enumerate(d):
        f += (-a) if i & 1 else a

    g = (-f if f < 0 else f) % len(s)
    g = len(s) - g if f < 0 else g

    # print(f, g)

    # ans = s[len(s) - g:] + s[:len(s) - g]
    ans = s[-g:] + s[:-g]
    # print(s, ans)

    with open(f'testcase/{ith}.in', 'w') as f:
        f.write(f'{n1}' + '\n' + ds + '\n' + s + '\n')

    with open(f'testcase/{ith}.out', 'w') as f:
        f.write(ans + '\n')

for i in range(t):
    generate_testcase(i + 1)
