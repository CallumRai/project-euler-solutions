from itertools import permutations

numbers = sorted(permutations(list(range(1,10))), reverse=True)

for x in numbers:
    no = ''
    for i in range(len(x)):
        no+=str(x[i])

    x = int(no)

    # 4,5 check
    num_1 = int(str(x)[0:4])
    num_2 = int(str(x)[4:])

    if num_1 == num_2 / 2:
        break

    # 3,3,3 check
    num_1 = int(str(x)[0:3])
    num_2 = int(str(x)[3:6])
    num_3 = int(str(x)[6:])

    if num_1 == num_2 / 2 == num_3 / 3:
        break

    # 2,2,2,3 check
    num_1 = int(str(x)[0:2])
    num_2 = int(str(x)[2:4])
    num_3 = int(str(x)[4:6])
    num_4 = int(str(x)[6:])

    if num_1 == num_2 / 2 == num_3 / 3 == num_4 / 4:
        break

    if x <= 918273645:
        x = 918273645
        break

    x -= 1

print(x)