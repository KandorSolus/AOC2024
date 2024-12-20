from functools import cmp_to_key
rules = []
cmp = (lambda x,y: 1-2*((x, y) in rules))
p = [0, 0]
def parseLine(text):
    if text == '':
        return
    rule = text.split('|')
    if (len(rule) > 1):
        rules.append((int(rule[0]), int(rule[1])))
    else:
        l = [int(x.strip()) for x in text.split(',')]
        s = sorted(l, key = cmp_to_key(cmp))
        p[s!=l] += s[(len(s) - 1)//2]

for line in open("5_1.txt", "r"):
    parseLine(line.strip())
print(p)