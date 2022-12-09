def process_move(line):
    parts = line.split()
    dir = parts[0]
    n = int(parts[1])
    for i in range(n):
        move(dir)


t_x = [0] * 10
t_y = [0] * 10
visits = set()


def update_tail(i):
    global t_x, t_y, visits
    d_x = t_x[i - 1] - t_x[i]
    d_y = t_y[i - 1] - t_y[i]
    # overlap
    if d_x == 0 and d_y == 0:
        return
    # touching
    if abs(d_x) == 1:
        if abs(d_y) == 1 or d_y == 0:
            return
    if abs(d_y) == 1:
        if abs(d_x) == 1 or d_x == 0:
            return
    # move to touch
    if d_x >= 1:
        t_x[i] += 1
    if d_x <= -1:
        t_x[i] -= 1
    if d_y >= 1:
        t_y[i] += 1
    if d_y <= -1:
        t_y[i] -= 1
    # print('\t', i, t_x, t_y)
    if i == 9:
        visits.add((t_x[i], t_y[i]))


def move(direction):
    if direction == 'R':
        t_x[0] += 1
    elif direction == 'L':
        t_x[0] -= 1
    elif direction == 'U':
        t_y[0] += 1
    elif direction == 'D':
        t_y[0] -= 1
    else:
        raise RuntimeError(f"Bad Direction {direction}")
    # print(t_x, t_y)
    for i in range(1, 10):
        update_tail(i)


with open('input') as f:
    visits.add((0, 0))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        process_move(line)

print(len(visits))
