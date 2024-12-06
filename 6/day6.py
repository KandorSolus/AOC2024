grid = []
startPos = (0, 0)
currDir = 0
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
allPos = set()
def turn():
    global currDir
    currDir = (currDir + 1) % 4
def parseGrid(i, text):
    global startPos
    row = list(text)
    if '^' in row:
        startPos = (row.index('^'), i)
    grid.append(row)
    
def facingOut(currPos):
    return currPos[1] == 0 and currDir == 0 or currPos[1] == h - 1 and currDir == 2 or currPos[0] == 0 and currDir == 3 or currPos[0] == w - 1 and currDir == 1
for i, line in enumerate(open("6_1.txt", "r")):
    parseGrid(i, line.strip())
w = len(grid[0])
h = len(grid)
def part1():
    currPos = startPos
    while not facingOut(currPos):
        allPos.add(currPos)
        nextPos = (currPos[0] + direction[currDir][0], currPos[1] + direction[currDir][1])
        if grid[nextPos[1]][nextPos[0]] == '#':
            turn()
        else:
            currPos = nextPos
    allPos.add(currPos)
    print(len(allPos))
loops = set()
def printGrid(grid):
    for row in grid:
        print(row)
def checkLoop():
    global currDir
    currPos = startPos
    currDir = 0
    allPos = set()
    while not facingOut(currPos):
        if (currPos, currDir) in allPos:
            return True
        allPos.add((currPos, currDir))
        nextPos = (currPos[0] + direction[currDir][0], currPos[1] + direction[currDir][1])
        if grid[nextPos[1]][nextPos[0]] == '#':
            turn()
        else:
            currPos = nextPos
    return False
def part2():
    for x in range(w):
        print(x)
        for y in range(h):
            if grid[y][x] == '#':
                continue
            else:
                grid[y][x] = '#'
                if checkLoop():
                    global loops
                    loops.add((x, y))
                grid[y][x] = '.'
    print(len(loops))
part1()
part2()
