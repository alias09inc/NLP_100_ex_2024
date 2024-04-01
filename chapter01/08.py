def cipher(st):
    ans = ''
    for i in st:
        if i >= 'a' and i <= 'z':
            ans += chr(219 - ord(i))
        else:
            ans += i
    return ans


a = input('Enter the word you wanna encrypt: ')

b = cipher(a)

print(a)
print(b)
