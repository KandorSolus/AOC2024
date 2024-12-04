def isValid(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def search(grid, x, y):
    if not all(isValid(grid, y+a, x+b) for b in [-1, 1] for a in [-1, 1]):
        return False
    fst = grid[y-1][x-1] == "M" and grid[y+1][x+1] == "S" or grid[y-1][x-1] == "S" and grid[y+1][x+1] == "M";
    snd = grid[y-1][x+1] == "M" and grid[y+1][x-1] == "S" or grid[y-1][x+1] == "S" and grid[y+1][x-1] == "M";
    return fst and snd

grid = [list(line.strip()) for line in open("4_1.txt", "r")]
part2 = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "A":
            part2 += search(grid, x, y)
print(part2)