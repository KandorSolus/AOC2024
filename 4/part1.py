directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def isValid(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def search(grid, x, y):
    sol = 0
    for a, b in directions:
        if (all(isValid(grid, y+a*(1+i), x+b*(1+i)) and grid[y+a*(1+i)][x+b*(1+i)] == c for i, c in enumerate("MAS"))):
            sol += 1
    return sol

grid = [list(line.strip()) for line in open("4_1.txt", "r")]
part1 = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "X":
            part1 += search(grid, x, y)
print(part1)