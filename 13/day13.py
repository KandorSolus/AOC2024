import re

games = open('13.txt', 'r').read().split('\n\n')
parsed_games = []
solution = [0, 0]
for game in games:
    pattern = r'Button A: X\+(\d+), Y\+(\d+)|Button B: X\+(\d+), Y\+(\d+)|Prize: X=(\d+), Y=(\d+)'
    matches = re.findall(pattern, game)

    a = (int(matches[0][0]), int(matches[0][1]))
    b = (int(matches[1][2]), int(matches[1][3]))
    p = (int(matches[2][4]), int(matches[2][5]))

    y = (p[0]*b[0]*a[1]-a[0]*p[1]*b[0])/(b[0]*(b[0]*a[1]-b[1]*a[0]))
    x = (p[1]*b[0]-b[1]*p[0])/(b[0]*a[1]-b[1]*a[0])

    p = (10000000000000+p[0], 10000000000000+p[1])

    y2 = (p[0]*b[0]*a[1]-a[0]*p[1]*b[0])/(b[0]*(b[0]*a[1]-b[1]*a[0]))
    x2 = (p[1]*b[0]-b[1]*p[0])/(b[0]*a[1]-b[1]*a[0])

    if int(x) == x and int(y) == y:
        solution[0] += int(3*x + y)
    if int(x2) == x2 and int(y2) == y2:
        solution[1] += int(3*x2 + y2)
print(solution)