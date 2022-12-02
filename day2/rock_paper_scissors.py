def decode(inp):
    switch = {
        'A': 'rock',
        'X': 'rock',
        'B': 'paper',
        'Y': 'paper',
        'C': 'scissors',
        'Z': 'scissors'
    }
    return switch.get(inp, f'Bad input {inp}')


def play(p1, p2):
    win = 6
    draw = 3
    loss = 0
    rock = 1
    paper = 2
    scissors = 3
    rock_s = 'rock'
    paper_s = 'paper'
    scissors_s = 'scissors'
    if p2 == rock_s:
        if p1 == rock_s:
            return ('D', draw+rock)
        if p1 == paper_s:
            return ('L', loss+rock)
        if p1 == scissors_s:
            return ('W', win+rock)
    if p2 == paper_s:
        if p1 == paper_s:
            return ('D', draw+paper)
        if p1 == rock_s:
            return ('W', win+paper)
        if p1 == scissors_s:
            return ('L', loss+paper)
    if p2 == scissors_s:
        if p1 == scissors_s:
            return ('D', draw+scissors)
        if p1 == paper_s:
            return ('W', win+scissors)
        if p1 == rock_s:
            return ('L', loss+scissors)


with open('input', 'r') as f:

    line = f.readline().strip()
    score = 0
    while line:
        elf, me = line.split()
        elf = decode(elf)
        me = decode(me)
        wdl = play(elf, me)
        score += wdl[1]
        line = f.readline().strip()

    print("score: ", score)
