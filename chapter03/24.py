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

data = data.split('\n')
print(len(data))

ans = [i for i in data if re.search(
    r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', i)]
# ([^]|]+?) : ]と|が直後に来るのを防ぐ？
'''
検証
>>> a = 'abcdefg|hij'
>>> re.search(r'ab([^|]+?)',a)
<re.Match object; span=(0, 3), match='abc'>
>>> re.search(r'ab([^|]+?)(\|)',a)
<re.Match object; span=(0, 8), match='abcdefg|'>
<re.Match object; span=(0, 8), match='abcdefg|'>
>>> re.search(r'ab([^|]+?)(\|.*?)+',a)
<re.Match object; span=(0, 8), match='abcdefg|'>
>>> re.search(r'ab([^|]+?)(\|.*?)+h',a)
<re.Match object; span=(0, 9), match='abcdefg|h'>
>>> re.search(r'ab([^|]+?)(\|.*?)+hij',a)
<re.Match object; span=(0, 11), match='abcdefg|hij'>
>>> a = 'abcdefg|aa|aa|hij'
>>> re.search(r'ab([^|]+?)(\|.*?)+hij',a)
<re.Match object; span=(0, 17), match='abcdefg|aa|aa|hij'>
'''
for i in ans:
    print(i)
