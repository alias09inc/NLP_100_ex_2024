def parse_mecab(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        (surface, attrs) = line.split('\t')
        attr = attrs.split(',')
        base = attr[6]
        pos = attr[0]
        pos1 = attr[1]
        linedict = {
            'surface': surface,
            'base': base,
            'pos': pos,
            'pos1': pos1,
        }
        res.append(linedict)


filename = 'neko.txt.mecab'
mapping_lists = []

with open(filename, mode='rt', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')
blocks = list(filter(lambda x: x!= '', blocks))
blocks = [parse_mecab(block) for block in blocks]

# ここからが31の開放
renketu_list = []
for block in blocks:
   for (idx, mapped_word) in enumerate(block):
       if mapped_word["surface"] =='の' and (0<idx and idx < len(block)-1) and block[idx-1]['pos'] == '名詞' and block[idx+1]['pos'] == '名詞':
           renketu_list.append(block[idx-1]['surface'] + 'の' + block[idx+1]['surface'])

print(renketu_list)