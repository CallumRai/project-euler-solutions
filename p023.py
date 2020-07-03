from math import ceil

divisors_dict = {}
for i in range(1, 28124):
    divisors = []
    for j in range(1, ceil(i / 2) + 1):
        if i % j == 0 and j < i:
            divisors.append(j)

    divisors_dict[i] = sum(divisors)

abundant = []
for key in divisors_dict.keys():
    if divisors_dict[key] > key:
        abundant.append(key)

abundant_sums = []
for i in abundant:
    for j in abundant:
        abundant_sums.append(i + j)

abundant_sums = list(set(abundant_sums))

cannot = []
for i in range(1, 28124):
    if i not in abundant_sums:
        cannot.append(i)

print(sum(cannot))
