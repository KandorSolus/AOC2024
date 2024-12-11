input = [list(map(int, list(line.strip()))) for line in list(open("10_1.txt", "r").readlines())]
count = 0
count2 = 0
def calc(x, y, p2 = False):
    global input
    currs = [(x, y)]
    while any(input[y][x] < 9 for x,y in currs):
        temp = []
        for x, y in currs:
            if input[y][x] == 9:
                temp.append((x, y))
            if y > 0 and input[y - 1][x] == (input[y][x] + 1):
                temp.append((x, y - 1))
            if y < (len(input) - 1) and input[y + 1][x] == (input[y][x] + 1):
                temp.append((x, y + 1))
            if x > 0 and input[y][x - 1] == (input[y][x] + 1):
                temp.append((x - 1, y))
            if x < (len(input[0]) - 1) and (input[y][x + 1] == (input[y][x] + 1)):
                temp.append((x + 1, y))
            if len(temp) == 1 and temp[0] == (x, y):
                temp = []
        currs = temp
    if p2:
        return len(currs)
    return len(set(currs))

for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == 0:
            count += calc(x, y)
            count2 += calc(x, y, True)
print(count)
print(count2)