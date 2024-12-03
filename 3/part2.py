import re
f = open("3_2.txt", "r")
def mult(m):
    match = re.search(r'([0-9]{1,3}),([0-9]{1,3})', m)
    return int(match.group(1))*int(match.group(2))

def multiply(text):
    text = text.replace('\n', ' ').replace('\r', '')
    text = re.sub(r'don\'t\(\).*?(?:do\(\)|$)', '', text)
    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', text)
    return sum(mult(match) for match in matches)
print(multiply(f.read()))