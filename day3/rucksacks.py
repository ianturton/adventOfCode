def get_score(ch):
    if ch.islower():
        base = ord('a')
        offset = 1
    else:
        base = ord('A')
        offset = 27
    val = ord(ch)
    if val < base:
        raise RuntimeError("bad val")
    return offset + val - base


with open('input') as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        size = len(line)//2
        first = line[:size]
        last = line[size:]
        contents = set()
        for c in first:
            contents.add(c)

        dup = '*'
        for c in last:
            if c in contents:
                dup = c
                break

        score = get_score(dup)
        total += score
    print(total)
