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
max_len_list = []
for block in blocks:
   i = 0
   tmp = ''
   while i < len(block):
      if block[i]['pos'] == '名詞':
          tmp += block[i]['surface']
      else:
          if tmp != '':
              max_len_list.append(tmp)
          tmp = ''
      i+=1
   if tmp != '':
      max_len_list.append(tmp)

print(max_len_list)
             