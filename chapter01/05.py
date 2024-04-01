import re

def make_n_gram(obj, n):
    ans = []
    for i in range(int(len(obj)/n+1)):
        ans.append(obj[i*2:(i+1)*2])
    return ans

a = "I am an NLPer"

word_gram = make_n_gram(re.split("[ ]", a), 2)
char_gram = make_n_gram(a, 2)

print(word_gram)
print(char_gram)