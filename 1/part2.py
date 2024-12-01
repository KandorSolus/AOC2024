f = open("1_2.txt", "r")
l = []
r = []
def addBoth(text):
    nums = text.split()
    l.append(int(nums[0]))
    r.append(int(nums[1]))

[addBoth(line) for line in f.readlines()]
print(sum([abs(x*r.count(x)) for x in l]))