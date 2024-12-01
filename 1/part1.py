import bisect
f = open("1_1.txt", "r")
l = []
r = []
def addBoth(text):
    nums = text.split()
    bisect.insort(l, int(nums[0]))
    bisect.insort(r, int(nums[1]))

[addBoth(line) for line in f.readlines()]
print(sum([abs(x-y) for x,y in zip(l, r)]))