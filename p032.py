digit_lengths = []
for i in range(1, 8):
    for j in range(1, 8):
        digit_lengths.append([i, j])

valid_digit_lengths = []
for length in digit_lengths:
    if sum(length) >= 9:
        break
    else:
        length.append(9 - sum(length))
        valid_digit_lengths.append(tuple(sorted(length)))

valid_digit_lengths = list(set(valid_digit_lengths))

lengths9 = []
for length in valid_digit_lengths:
    lower_bdd = len(str((10 ** (length[0] - 1)) * (10 ** (length[1] - 1))))
    upper_bdd = len(str((10 ** (length[0]) - 1) * (10 ** (length[1]) - 1)))

    if lower_bdd <= length[2] <= upper_bdd:
        lengths9.append(length)

numbers9 = []
for length in lengths9:
    numbers1 = list(range(10 ** (length[0] - 1), 10 ** (length[0])))
    numbers2 = list(range(10 ** (length[1] - 1), 10 ** (length[1])))

    for i in numbers1:
        for j in numbers2:
            number3 = i * j

            if len(str(number3)) == length[2]:
                numbers9.append(tuple([i, j, number3]))

pandigital_comb = []
for comb in numbers9:
    numbers = []
    number1 = str(comb[0])
    number2 = str(comb[1])
    number3 = str(comb[2])

    for number in [number1, number2, number3]:
        for i in range(len(number)):
            if int(number[i]) != 0:
                numbers.append(int(number[i]))

    if len(set(numbers)) == 9:
        pandigital_comb.append(comb)

products = []
for comb in pandigital_comb:
    products.append(comb[2])

products = list(set(products))

cumsum = 0
for product in products:
    cumsum += product

print(cumsum)