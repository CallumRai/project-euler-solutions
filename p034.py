def fact(no):
    if no == 0 or no == 1:
        return 1

    numbers = list(range(2, no + 1))

    i = 1
    for number in numbers:
        i = i * number

    return i


found = False
i = 2

while not found:
    i += 1
    if fact(9) * i < 10 ** (i - 1):
        i -= 1
        found = True
        break

numbers = []
for j in range(10, 10**i):

    cumsum = 0
    for k in range(len(str(j))):
        cumsum += fact(int(str(j)[k]))
        if cumsum > j:
            break

    if cumsum == j:
        numbers.append(j)

print(sum(numbers))