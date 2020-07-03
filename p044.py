def get_pentagon(n):
    pentagons = []
    for i in range(1, n + 1):
        pentagons.append(i * (3 * i - 1) / 2)

    return pentagons

x = 500
pentagons = get_pentagon(x)
found = False

while not found:
    for i in range(x):
        for j in range(x):
            if i < x - 500 and j < x - 500:
                continue

            if pentagons[i] + pentagons[j] in pentagons and abs(pentagons[i] - pentagons[j]) != 0 and \
                    abs(pentagons[i] - pentagons[j]) in pentagons:
                found = True
                print(int(abs(pentagons[i] - pentagons[j])))

    if not found:
        x += 500
        pentagons = get_pentagon(x)
