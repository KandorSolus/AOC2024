import re
f = open("3_1.txt", "r")
def mult(m):
    match = re.search(r'([0-9]{1,3}),([0-9]{1,3})', m)
    return int(match.group(1))*int(match.group(2))

def multiply(text):
    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', text)
    return sum(mult(match) for match in matches)
print(sum(multiply(line) for line in f.readlines()))