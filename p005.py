i = 20
test = False

while not test:
    found = True

    for j in range(2, 21):
        if i % j != 0:
            i += 20
            found = False
            break

    if found:
        test = True

print(i)