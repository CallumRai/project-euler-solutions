from math import sqrt, floor

triples = []
for i in range(1, 1001):
    for j in range(1, 1001):
        if floor(sqrt(i**2 + j**2)) == sqrt(i**2 + j**2):
            triples.append(tuple(sorted([i,j,sqrt(i**2 + j**2)])))

triples = list(set(triples))

freq = []
for triple in triples:
    if sum(triple) <= 1000:
        freq.append(sum(triple))

freq_dict = {}
for i in range(1001):
    freq_dict[i] = 0

for f in freq:
    freq_dict[f] += 1

print(max(freq_dict, key=freq_dict.get))