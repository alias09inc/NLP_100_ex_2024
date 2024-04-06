import json
import re

decoder = json.JSONDecoder()

with open('jawiki-country.json', 'r') as f:
    line = f.readline()
    while line:
        line_json = decoder.decode(line)
        country_name = line_json['title']
        if country_name != 'イギリス':
            line = f.readline()
        else:
            print(country_name)
            # print(line_json['text'])
            data = line_json['text']
            break

data = re.search(r'''
    ^\{\{基本情報.*?\n
    (.*?)
    \}\}
    $
''', data, re.MULTILINE+re.VERBOSE+re.DOTALL)
print(data)
