import re
from collections import OrderedDict
from pprint import pprint
import pandas as pd

def extract_by_title(title):
    df_wiki = pd.read_json('jawiki-country.json', lines=True)
    return df_wiki[(df_wiki['title'] == title)]['text'].values[0]

wiki_body = extract_by_title('イギリス')

basic = re.search(r'''
                    ^\{\{基礎情報.*?\n  #検索語句(\はエスケープ処理)、非キャプチャ、非貪欲
                    (.*?)              #任意の文字列
                    \}\}               #検索語句(\はエスケープ処理)
                    $                  #文字列の末尾
                    ''', wiki_body, re.MULTILINE+re.VERBOSE+re.DOTALL)
# print(basic.group(1))

results = re.findall(r'''
                        ^\|
                        (.*?)
                        \s*
                        =
                        \s*
                        (.*?)
                        (?:
                            (?=\n\|)
                        |   (?=\n$)
                        )
                        ''', basic.group(1), re.MULTILINE+re.VERBOSE+re.DOTALL)

result_dict = OrderedDict(results)

def remove_markup(string):
    replaced = re.sub(r'''
                        (\'{2,5})
                        (.*?)
                        (\1)
                        ''', r'\2', string, flags=re.MULTILINE+re.VERBOSE)#r'\2'=>二つ目のマッチングに置き換える=>1個目と3個目の要素を削除
    return replaced

for i, (key, value) in enumerate(result_dict.items()):
    replaced = remove_markup(value)
    result_dict[key] = replaced

    # 変わったものを表示
    if value != replaced:
        print(i, key) 
        print('変更前\t', value)
        print('変更後\t', replaced)
        print('----')

pprint(result_dict)