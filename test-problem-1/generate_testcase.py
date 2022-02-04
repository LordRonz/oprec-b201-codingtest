from random import choice, randint, shuffle
t = 8

def gen_num(odd = True):
    a = randint(1, 100)
    while a % 2 == (0 if odd else 1):
        a = randint(1, 100)
    return a

def generate_testcase(ith = 1):
    sus_odd = choice((True, False))
    n = randint(3, 100)
    nums = [gen_num(not sus_odd) for _ in range(n - 1)]
    nums.append(gen_num(sus_odd))
    shuffle(nums)

    assert len([a for a in nums if a % 2 == (1 if sus_odd else 0)]) == 1

    ans = 0
    for i, a in enumerate(nums):
        if a % 2 == (1 if sus_odd else 0):
            ans = i
            break

    with open(f'{ith}.in', 'w') as f:
        f.write(f'{n}\n' + ' '.join(f'{a}' for a in nums) + '\n')

    with open(f'{ith}.out', 'w') as f:
        f.write(f'{ans}\n')

for i in range(t):
    generate_testcase(i + 1)
