def is_visible(grid, i, j):
    # A tree is not visible iff all the trees between
    # it and the edge are shorter than it is
    height = grid[i][j]
    row = grid[i]
    col = []
    for x in range(0, len(grid)):
        col.append(grid[x][j])
    # print(i, j, height, grid[i])
    rsum1 = [s for s in row[:j] if s >= height]
    rsum2 = [s for s in row[j + 1:] if s >= height]
    csum1 = [s for s in col[:i] if s >= height]
    csum2 = [s for s in col[i + 1:] if s >= height]

    # print(i, j, height)
    # print('r', row[:j], row[j + 1:])
    # print('c', col[:i], col[i + 1:])
    # print((rsum1), (rsum2))
    # print((csum1), (csum2))
    ret = bool(len(rsum1)) and bool(len(rsum2)) and \
        bool(len(csum1)) and bool(len(csum2))
    # print(not ret)
    return bool(not ret)


def scenic_score(grid, i, j):
    # A tree is not visible iff all the trees between
    # it and the edge are shorter than it is
    height = grid[i][j]
    row = grid[i]
    col = []
    for x in range(0, len(grid)):
        col.append(grid[x][j])
    # print(i, j, height)

    left = []
    for r in reversed(row[:j]):
        left.append(r)

    right = row[j + 1:]
    up = []
    for u in reversed(col[:i]):
        up.append(u)
    down = col[i + 1:]
    # print(left[:], right)
    # print(up[:], down)
    score = []
    score.append(scorer(height, left))
    score.append(scorer(height, right))
    score.append(scorer(height, up))
    score.append(scorer(height, down))
    # print(score)
    sum = 1
    for s in score:
        sum *= s
    return sum


def scorer(height, view):
    score = 0
    for v in view:
        score += 1
        if v >= height:
            break
    return score


def part1(grid):
    result = []
    for i in range(0, len(grid)):
        result.append([])
        for j in range(0, len(grid[i])):
            result[i].append(is_visible(grid, i, j))

    count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if result[i][j]:
                count += 1
        #  print(result[i][j], end=' ')
        # print()

    print(count)


def part2(grid):
    result = []
    max = -1
    for i in range(0, len(grid)):
        result.append([])
        for j in range(0, len(grid[i])):
            res = scenic_score(grid, i, j)
            if res > max:
                max = res
            result[i].append(res)

    print(max)


with open('input') as f:
    lines = f.readlines()

grid = []
for line in lines:
    row = []
    for ch in line.strip():
        row.append(int(ch))
    grid.append(row)
# for i in range(0, len(grid)):
    # for j in range(0, len(grid[i])):
    # print(grid[i][j], end=' ')
    # print()

# part1(grid)
part2(grid)
