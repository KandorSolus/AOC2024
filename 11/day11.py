from collections import Counter

input = list(map(int, open("11_1.txt", "r").read().strip().split(" ")))
counted = Counter(input)
for _ in range(75):
    new_count = Counter()
    for k, v in counted.items():
        if k == 0:
            new_count[1] += v
        elif len(str(k)) % 2 == 0:
            center = len(str(k))//2
            new_count[int(str(k)[:center])] += v
            new_count[int(str(k)[center:])] += v
        else:
            new_count[2024*int(k)] += v
    counted = new_count
print(sum(counted.values()))