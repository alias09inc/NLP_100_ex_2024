import random

target = input()

lis_target = target.split()

print(lis_target)

ans = ''
for i in lis_target:
    if len(i) <= 4:
        ans += i + ' '
    else :
        tmp = random.sample(i[1:-1], len(i[1:-1]))
        ans += i[0] + ''.join(tmp) + i[-1] + ' '
print(ans)
        