def process_move(line):
    parts = line.split()
    dir = parts[0]
    n = int(parts[1])
    for i in range(n):
        move(dir)


h_x = 0
h_y = 0
t_x = 0
t_y = 0
visits = set()


def update_tail():
    global h_x, h_y, t_x, t_y, visits
    d_x = h_x - t_x
    d_y = h_y - t_y
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
        t_x += 1
    if d_x <= -1:
        t_x -= 1
    if d_y >= 1:
        t_y += 1
    if d_y <= -1:
        t_y -= 1
    # print('\t', t_x, t_y)
    visits.add((t_x, t_y))


def move(direction):
    global h_x, h_y
    if direction == 'R':
        h_x += 1
    elif direction == 'L':
        h_x -= 1
    elif direction == 'U':
        h_y += 1
    elif direction == 'D':
        h_y -= 1
    else:
        raise RuntimeError(f"Bad Direction {direction}")
    # print(h_x, h_y)
    update_tail()


with open('input') as f:
    visits.add((0, 0))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        process_move(line)

print(len(visits))
