def read_inputs(f):
    """
    Read in initial stack
            [H]         [S]         [D]
        [S] [C]         [C]     [Q] [L]
        [C] [R] [Z]     [R]     [H] [Z]
        [G] [N] [H] [S] [B]     [R] [F]
    [D] [T] [Q] [F] [Q] [Z]     [Z] [N]
    [Z] [W] [F] [N] [F] [W] [J] [V] [G]
    [T] [R] [B] [C] [L] [P] [F] [L] [H]
    [H] [Q] [P] [L] [G] [V] [Z] [D] [B]
     1   2   3   4   5   6   7   8   9
    """

    s = [""] * 9
    while True:
        # can't use strip because white space is important
        line = f.readline().replace('\n', '')+' '
        print(line)
        if not line.strip():
            break
        for i in range(0, len(line), 4):
            s[i//4] = s[i//4]+line[i: i+4]

    stacks = [None]*10
    i = 1
    for st in s:
        # strip the number from the end and reverse the order
        parts = st.split()
        stacks[i] = []
        for p in parts:
            if '[' in p:
                p = p.strip(' []')
                stacks[i].insert(0, p)
        i += 1

    moves = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        parts = line.split()
        n = int(parts[1])
        orig = int(parts[3])
        dest = int(parts[5])
        moves.append((n, orig, dest))
    return (stacks, moves)


def move_boxes(stacks, orig, dest, n):
    o = stacks[orig]
    d = stacks[dest]

    for i in range(n):
        box = o.pop()
        d.append(box)


with open('input') as f:
    stacks, moves = read_inputs(f)

    for m in moves:
        move_boxes(stacks, m[1], m[2], m[0])

    for s in stacks[1:]:
        print(s[-1], end='')
    print('')
