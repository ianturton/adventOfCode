def create_range(section):
    p = section.split('-')
    # ret = set(range(int(p[0]), int(p[1])+1))
    return (int(p[0]), int(p[1]))


with open('input') as f:
    count = 0
    while True:
        line = f.readline().strip()
        if not line:
            break
        parts = line.split(',')
        a = create_range(parts[0])
        b = create_range(parts[1])
        if a[0] <= b[0] and a[1] >= b[1]:
            count += 1
        elif b[0] <= a[0] and b[1] >= a[1]:
            count += 1

    print(count)
