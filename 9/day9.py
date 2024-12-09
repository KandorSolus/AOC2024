input = list(map(int, list(open("9_1.txt", "r").read().strip())))
input_size = sum(input)
output = ["."]  * input_size
fid = 0
idx = 0
file = True
for  x in input:
    if file:
        for i in range(idx, idx + x):
            output[i] = fid
        fid += 1
    idx += x
    file = not file

i = input_size - 1
for fid in output[::-1]:
    if fid != ".":
        free = output.index(".")
        if free < i:
            output[i], output[free] = (output[free], output[i])
        else:
            break
    i -= 1
print(sum(i * x for i, x in enumerate(output) if x != "."))