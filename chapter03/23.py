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

data = data.split('\n')
print(len(data))

ans = [i for i in data if re.search(r'==.*==',i)]
print(ans)
for i in ans:
    if re.match(r'==[^=].',i):
        print(1,i.replace('==',''))
    elif re.match(r'===[^=].',i):
        print(2,i.replace('===',''))
    elif re.match(r'====[^=].',i):
        print(3,i.replace('====',''))
