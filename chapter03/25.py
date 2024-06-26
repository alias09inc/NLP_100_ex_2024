import re
import pandas as pd

df = pd.read_json('jawiki-country.json', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
text = text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
for line in text:
    r = re.search(pattern, line)
    if r:
        ans[r[1]] = r[2]

for k, v in ans.items():
    print(k, v)
