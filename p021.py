from math import ceil

divisors_dict = {}
for i in range(1, 10001):
    divisors = []
    for j in range(1, ceil(i / 2) + 1):
        if i % j == 0 and j < i:
            divisors.append(j)

    divisors_dict[i] = sum(divisors)

amicable = []
for key in divisors_dict.keys():
    try:
        if key == divisors_dict[divisors_dict[key]] and key != divisors_dict[key]:
            amicable.append(key)
    except KeyError:
        continue

print(sum(amicable))
