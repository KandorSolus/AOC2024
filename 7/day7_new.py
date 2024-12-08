f = open("7_1.txt", "r")
def canConcat(num, num2):
    if num in (num2, -num2):
        return False
    return str(num).endswith(str(num2))

def conc(num, num2):
    return int(str(num) + str(num2))

def parseLine(text):
    res, p = text.split(':')
    res = int(res)
    p = list(map(int, map(str.strip, p.split())))
    return res if resolve(res, p) > 0 else 0
    
def resolve(res, p):
    if res < 0:
        return 0
    p2 = p[:]
    n = p2.pop()
    c = 0
    if len(p2) == 1:
        if p2[0] * n == res:
            c += 1
        if p2[0] + n == res:
            c += 1
        if conc(p2[0], n) == res<:
            c += 1
        return c
    if res % n == 0:
        c += resolve(res//n, p2)
    if canConcat(res, n):
        c += resolve(int(str(res)[:-len(str(n))]), p2)
    c += resolve(res - n, p2)
    return c
print(sum(parseLine(line.strip()) for line in f.readlines()))