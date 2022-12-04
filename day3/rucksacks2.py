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
    while True:
        contents_list = []
        for i in range(3):
            line = f.readline()
            line = line.strip()
            if not line:
                break

            contents = set()
            for c in line:
                contents.add(c)

            contents_list.append(contents)

        if not contents_list:
            break
        dup = contents_list[0] & contents_list[1] & contents_list[2]
        score = get_score(dup.pop())
        total += score
    print(total)
