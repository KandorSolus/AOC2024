f = open("8_1.txt", "r")
d = {}
w = 0
h = 0
def parseLine(line, i):
    global w, h
    y = i
    l = list(line)
    w = len(l)
    h = i + 1
    for x in range(len(l)):
        if l[x] != '.':
            if not l[x] in d:
                d[l[x]] = [(x, y)]
            else:
                d[l[x]].append((x, y))

for i, line in enumerate(f.readlines()):
    parseLine(line.strip(), i)
s = set()
for k in d:
    for a in d[k]:
        for b in d[k]:
            if a != b:
                mi = (b[0], b[1])
                diff = (a[0]-b[0], a[1]-b[1])
                while 0 <= mi[0] < w and 0 <= mi[1] < h:
                    mi = (mi[0]-diff[0], mi[1]-diff[1])
                    if 0 <= mi[0] < w and 0 <= mi[1] < h:
                        s.add(mi)
                ma = (a[0], a[1])
                while 0 <= ma[0] < w and 0 <= ma[1] < h:
                    ma = (ma[0]+diff[0], ma[1]+diff[1])
                    if 0 <= ma[0] < w and 0 <= ma[1] < h:
                        s.add(ma)
                s.add(a)
                s.add(b)
print(len(s))
  