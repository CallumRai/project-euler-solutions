def pentagon_dict(prev_dict, n):
    start = len([j for i, j in prev_dict.items() if j])

    for i in range(start-1, n + 1):
        prev_dict[i * (3 * i - 1) / 2] = True

    return prev_dict


def hexagon_dict(prev_dict, n):
    start = len([j for i, j in prev_dict.items() if j])

    for i in range(start-1, n + 1):
        prev_dict[i * (2 * i - 1)] = True

    return prev_dict


pent_dict = pentagon_dict({}, 1)
hex_dict = hexagon_dict({}, 1)
found = False
i = 1

while not found:
    x = i * (i + 1) / 2

    pent_dict = pentagon_dict(pent_dict, i)
    hex_dict = hexagon_dict(hex_dict, i)

    if i == 285 or i == 1:
        i += 1
        continue

    if pent_dict.get(x) == True and hex_dict.get(x) == True:
        found = True
        print(x)

    i += 1
