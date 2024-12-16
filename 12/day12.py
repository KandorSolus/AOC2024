grid = []
for line in open('12.txt', 'r').readlines():
    grid.append(list(line.strip()))
w = len(grid[0])
h = len(grid)
searched = set()
def test(grid, x, y, seen, c):
    if grid[y][x] == c:
        if (x, y) not in seen:
            return search(grid, x, y, seen)
        else:
            return (0, 0, seen)
    else:
        return (0, 1, seen)
def search(grid, x, y, seen = set()):
    s = 0
    f = 0
    c = grid[y][x]
    seen.add((x,y))
    if y == 0:
        f += 1
        s1, f1, see = test(grid, x, y + 1, seen, c)
        s += s1
        f += f1
        seen.update(see)
    elif y == h - 1:
        f += 1
        s1, f1, see = test(grid, x, y - 1, seen, c)
        s += s1
        f += f1
        seen.update(see)
    else:
        s1, f1, see = test(grid, x, y + 1, seen, c)
        s += s1
        f += f1
        seen.update(see)
        s1, f1, see = test(grid, x, y - 1, seen, c)
        s += s1
        f += f1
        seen.update(see)
    if x == 0:
        f += 1
        s1, f1, see = test(grid, x + 1, y, seen, c)
        s += s1
        f += f1
        seen.update(see)
    elif x == w - 1:
        f += 1
        s1, f1, see = test(grid, x - 1, y, seen, c)
        s += s1
        f += f1
        seen.update(see)
    else:
        s1, f1, see = test(grid, x + 1, y, seen, c)
        s += s1
        f += f1
        seen.update(see)
        s1, f1, see = test(grid, x - 1, y, seen, c)
        s += s1
        f += f1
        seen.update(see)
    return (1+s, f, seen)
s = 0
for y in range(h):
    for x in range(w):
        if (x, y) not in searched:
            (s1, f1, see) = search(grid, x, y)
            s += s1 * f1
            searched.update(see)
print(s)