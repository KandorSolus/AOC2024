import re
from numpy import prod
w = 101
h = 103
positions = []
for line in open('14.txt', 'r').readlines():
    pattern = r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)'
    match = re.match(pattern, line.strip())
    if match:
        p1, p2, v1, v2 = match.groups()
        positions.append([(int(p1)+100*int(v1))%w, (int(p2)+100*int(v2))%h])
safety = [0, 0, 0, 0]
for p in positions:
    if p[0] < w//2 and p[1] < h//2:
        safety[0] += 1
    if p[0] > w//2 and p[1] < h//2:
        safety[1] += 1
    if p[0] < w//2 and p[1] > h//2:
        safety[2] += 1
    if p[0] > w//2 and p[1] > h//2:
        safety[3] += 1
print(prod(safety))

positions = []
velocities = []
for line in open('14.txt', 'r').readlines():
    pattern = r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)'
    match = re.match(pattern, line.strip())
    if match:
        p1, p2, v1, v2 = match.groups()
        positions.append([int(p1), int(p2)])
        velocities.append([int(v1), int(v2)])
steps = 0
pos_len = len(positions)

safety = [0,0,0,0]
min_safety = 100_000_000_000_000
while not any(list(map(lambda x: x > pos_len/2, safety))) and steps < 10000:
    steps += 1
    safety = [0,0,0,0]
    for i, pos in enumerate(positions):
        v = velocities[i]
        p = [(pos[0]+v[0])%w, (pos[1]+v[1])%h]
        positions[i] = p
        if p[0] < w//2 and p[1] < h//2:
            safety[0] += 1
        if p[0] > w//2 and p[1] < h//2:
            safety[1] += 1
        if p[0] < w//2 and p[1] > h//2:
            safety[2] += 1
        if p[0] > w//2 and p[1] > h//2:
            safety[3] += 1
print(steps)