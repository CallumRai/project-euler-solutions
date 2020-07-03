grid = [[0] * 1001 for i in range(1002)]

pos = [500, 500]
grid[pos[0]][pos[1]] = 1
clock = [[0, 1], [-1, 0], [0, -1], [1, 0]]
direction = 0
n = 1
num = 2
full = False

while not full:

    valid = False
    while not valid:
        pos_temp = [pos[0] + clock[direction][0], pos[1] + clock[direction][1]]
        if abs(pos_temp[0] - 500) > n or abs(pos_temp[1] - 500) > n:
            if direction == 3:
                direction = 0
            else:
                direction += 1

        else:
            if grid[pos_temp[0]][pos_temp[1]] != 0:
                n += 1
                direction = 0
            else:
                pos = pos_temp
                valid = True

    grid[pos[0]][pos[1]] = num
    num += 1
    if num == 1001 ** 2 + 1:
        break

diagonals = []

for i in range(1001):
    diagonals.append(grid[i][i])
    diagonals.append(grid[i][1000 - i])

print(sum(diagonals)-1)