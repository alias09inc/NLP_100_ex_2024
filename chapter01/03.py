import re

a = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

b = re.split('[, .]', a)
print(b)

for i in b:
    if i != '':
        print(len(i))