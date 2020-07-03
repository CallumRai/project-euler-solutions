def fact(no):
    numbers = list(range(2, no + 1))

    i = 1
    for number in numbers:
        i = i * number

    return i

fact100 = str(fact(100))

cumsum = 0
for i in range(len(fact100)):
    cumsum += int(fact100[i])

print(cumsum)