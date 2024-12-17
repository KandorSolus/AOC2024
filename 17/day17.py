program = []
output = []

def checkNum(a, n):
    global program
    ptr = B = C = 0
    output = 0
    while ptr < len(program) - 1:
        jumped = False
        opcode = program[ptr]
        operand = program[ptr + 1]
        op = operand
        match operand:
            case 4:
                op = a
            case 5:
                op = B
            case 6:
                op = C
        match opcode:
            case 0:
                a = a//(2**op)
            case 1:
                B = B ^ operand
            case 2:
                B = op % 8
            case 3:
                if a != 0:
                    jumped = True
                    ptr = operand
            case 4:
                B = B ^ C
            case 5:
                out = op % 8
                if op >= 0:
                    if (program[len(program) - n + output] != out):
                        return 0
                    output += 1
                    if output == n:
                        return 1
                else:
                    print('ERROR')
                    return -1
            case 6:
                B = a//(2**op)
            case 7:
                C = a//(2**op)
        if not jumped:
            ptr += 2
    return 0

def findNum(a, n):
    global program
    if (n > len(program)):
        return a
    for i in range(8):
        if checkNum(a * 8 + i, n):
            res = findNum(a * 8 + i, n + 1)
            if res >= 0:
                return res
    return -1
    
for line in open('17.txt', 'r').readlines():
    if line.startswith('Register'):
        parts = line.strip().split(':')
        match (parts[0][-1:]):
            case 'A':
                A = int(parts[1].strip())
            case 'B':
                B = int(parts[1].strip())
            case 'C':
                C = int(parts[1].strip())
    elif line.startswith('Program'):
        parts = line.strip().split(':')
        program = list(map(int, parts[1].strip().split(',')))
solution = findNum(0, 1)
print(solution)