f = open("7_1.txt", "r")
def addOn(num, l):
    a = [x+num for x in l]
    b = [x*num for x in l]
    c = [int(str(x) + str(num)) for x in l]
    return a + b + c
def parseLine(text):
    print(text)
    res, p = text.split(':')
    res = int(res)
    p = list(map(int, map(str.strip, p.split())))
    print(res, p)
    res2 = [p[0]]
    for i in range(len(p) - 1):
        res2 = addOn(p[i + 1], res2)
    return res if res in res2 else 0
print(sum(parseLine(line.strip()) for line in f.readlines()))