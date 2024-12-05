rules = []
def all_rules(l, num, i):
    for x, y in rules:
        if x == num:
            if y in l and l.index(y) < i:
                return False
    return True
def parseLine(text):
    if text == '':
        return 0
    rule = text.split('|')
    if (len(rule) > 1):
        rules.append((int(rule[0]), int(rule[1])))
        return 0
    else:
        l = [int(num.strip()) for num in text.split(',')]
        if all(all_rules(l, num, i) for i, num in enumerate(l)):
            return l[(len(l) - 1)//2]
    return 0
        
print(sum(parseLine(line.strip()) for line in open("5_1.txt", "r")))