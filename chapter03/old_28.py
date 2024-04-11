import re
import pandas as pd


def remove_stress(dc):
    r = re.compile("'+")
    return {k: r.sub('', v) for k, v in dc.items()}


def remove_inner_links(dc):
    r = re.compile('\[\[(.+\||)(.+?)\]\]')
    return {k: r.sub(r'\2', v) for k, v in dc.items()}
    # \2で２つ目のマッチを残すように設定している


'''
作戦:標語や国名はパターンマッチの3つめを採用したい
refで囲まれている範囲は削除
国家はGod Save the Queenのみを残す
{{0}}は0にする

'''


def delete_wiki_markup(value):
    r0 = re.compile('\{\{(.+?)\|(.+?)\|(.+?)\|(.+?)[\}\)]+')
    value = r0.sub(r'\2', value)
    r1 = re.compile('\{\{(.+?)\|(.+?)\|(.+?)[\}\)]+')
    value = r1.sub(r'\3', value)
    r2 = re.compile('\{\{(.+?)\|(.+?)\|(.+?)\)')
    value = r2.sub(r'', value)
    return value


df = pd.read_json('jawiki-country.json', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
text = text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
for line in text:
    r = re.search(pattern, line)
    if r:
        ans[r[1]] = r[2]

ans = remove_stress(ans)
ans = remove_inner_links(ans)
for k, v in ans.items():
    print(k, delete_wiki_markup(v))
