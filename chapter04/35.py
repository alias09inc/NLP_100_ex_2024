from collections import defaultdict

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
d = defaultdict(int)

for block in blocks:
    for mapped_word in block:
        d[mapped_word['base']] += 1

ans = sorted(d.items(), key=lambda x:x[1], reverse=True)
print(ans)