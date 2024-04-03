import json
import re

decoder = json.JSONDecoder()

with open('jawiki-country.json', 'r') as f:
    line = f.readline()
    while line:
        line_json=decoder.decode(line)
        country_name = line_json['title']
        if country_name != 'イギリス':
            line = f.readline()
        else:
            print(country_name)
            # print(line_json['text'])
            data = line_json['text']
            break

print(type(data))

data = data.split('\n')

ans = list(filter(lambda x: '[Category:' in x, data))
print(ans)

ans = [i.replace('[[Category:','').replace('|*','').replace(']]','') for i in ans]
print(ans)