from random import choice, randint
t = 20

def gen_char():
    return choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def generate_testcase(ith = 1):
    n = randint(2, 169)
    s = ''.join(gen_char() for _ in range(n))

    low_cnt = len([a for a in s if a > 'Z'])
    up_cnt = len(s) - low_cnt

    ans_cnt = [0, 0, 0]

    res = ''
    if low_cnt > up_cnt:
        res = 'LOW'
        ans_cnt[0] = 1
    elif low_cnt < up_cnt:
        res = 'HI'
        ans_cnt[1] = 1
    else:
        res = 'SAME'
        ans_cnt[2] = 1

    with open(f'testcase/{ith}.in', 'w') as f:
        f.write(s + '\n')

    with open(f'testcase/{ith}.out', 'w') as f:
        f.write(res + '\n')
    return ans_cnt

hi = 0
low = 0
same = 0
for i in range(t):
    a, b, c = generate_testcase(i + 1)
    hi += a
    low += b
    same += c

print(hi, low, same)
