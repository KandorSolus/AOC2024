input = list(map(int, list(open("9_1.txt", "r").read().strip())))
input.append(0)
input_size = sum(input)
files = input[::2]
frees = input[1::2]
combination = zip(files, frees)
output = []
for i, (file, free) in enumerate(combination):
    output += [(file>0)*i]*abs(file)
    files[i] = 0
    # check if any file fits
    while free and any(0<t_file<=free for t_file in files):
        # check if file fits in reverse order
        for i in reversed(range(len(files))):
            if 0<files[i]<=free:
                output+=[i]*files[i]
                # reduce free by filesize
                free-=files[i]
                # mark as used
                files[i]*=-1
    output += [0]*free
print(sum(x*y for x, y in enumerate(output)))