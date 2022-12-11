
def report_value(cycle):
    global reg

    strength = 0
    if not (cycle - 20) % 40:
        strength = cycle * reg
        print(cycle, reg, strength)

    return strength


def draw_pixel(cycle):
    global reg
    global crt
    row = cycle // 40
    pos = (cycle - 1) % 40
    offset = reg - pos
    print(f"{row=}, {pos=}, {offset=}, {cycle=}, {reg=}")
    if abs(offset) <= 1:
        crt[row][pos] = '#'


def print_crt():
    global crt

    for c in range(len(crt)):
        print(c, ''.join(crt[c]))


with open('input') as f:
    lines = f.readlines()

cycle = 0
reg = 1
sum = 0
crt = []
for i in range(6):
    crt.append(['.'] * 40)

for line in lines:
    line = line.strip()
    cycle += 1
    sum += report_value(cycle)
    draw_pixel(cycle)
    print_crt()
    parts = line.split()
    op = parts[0]
    if op == 'noop':
        continue
    n = int(parts[1])
    cycle += 1
    sum += report_value(cycle)
    draw_pixel(cycle)
    print_crt()
    reg += n

print(sum)
