from random import choice, randint
t = 30

def gen_rand_str():
    return choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def gen_str(l, p = False):
    if not p and l > 1:
        s = ''.join(gen_rand_str() for _ in range(l))
        while s == s[::-1]:
            s = ''.join(gen_rand_str() for _ in range(l))
        return s

    s = ''.join(gen_rand_str() for _ in range(l//2))
    r = s
    if l & 1:
        s += gen_rand_str()

    s += r[::-1]
    return s

def generate_testcase(ith = 1):
    pal = choice((True, False))
    l = randint(3, 369)
    s = gen_str(l, p=pal)

    if pal:
        assert s == s[::-1]
    else:
        assert s != s[::-1]
    
    diff = 0
    a, b = 0, len(s) - 1
    while a < b:
        if s[a] != s[b]:
            diff += 1
        a += 1
        b -= 1

    ans = 'kasur nababan rusak' if pal else f'anta baka\n{diff}'

    with open(f'{ith}.in', 'w') as f:
        f.write(s + '\n')

    with open(f'{ith}.out', 'w') as f:
        f.write(ans + '\n')

for i in range(t):
    generate_testcase(i + 1)
