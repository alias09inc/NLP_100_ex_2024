import re

a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

ary = [0, 4, 5, 6, 7, 8, 14, 15, 18]

b = re.split('[, .]',a)
c = [i for i in b if i !='']
print(c)

ans = []

for i in range(len(c)):
    if i in ary:
        ans.append(c[i][0])
    else:
        ans.append(c[i][0:2])

print(ans)
