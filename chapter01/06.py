import re

def make_n_gram(obj, n):
    ans = []
    for i in range(int(len(obj)/n+1)):
        opr = obj[i*2:(i+1)*2]
        if opr != '' and opr != []:
            ans.append(opr)
    return ans

a = 'paraparaparadise'
b = 'paragraph'

bi_a = set(make_n_gram(a,2))
bi_b = set(make_n_gram(b,2))

print(bi_a,bi_b)

print(bi_a | bi_b)

print(bi_a & bi_b)

print(bi_a - bi_b)

print(bi_b - bi_a)

print('se' in bi_a)

print('se' in bi_b)