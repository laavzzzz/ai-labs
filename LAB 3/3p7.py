lst = [1, 2, 2, 3, 3, 3, 4]
freq = {}

for item in lst:
    freq[item] = freq.get(item, 0) + 1

print(freq)
