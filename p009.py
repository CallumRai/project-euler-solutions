squares_1000 = []
found = False
i = 1

while not found:
    squares_1000.append(i**2)
    i+=1
    if i >999:
        found=True

pythag_triple = []
for number1 in squares_1000:
    for number2 in squares_1000:
        if number1 == number2:
            continue

        if number1+number2 in squares_1000:
            pythag_triple.append([number1,number2,number1+number2])

for triple in pythag_triple:
    a = squares_1000.index(triple[0])+1
    b = squares_1000.index(triple[1])+1
    c = squares_1000.index(triple[2])+1

    if a+b+c == 1000:
        print(a*b*c)