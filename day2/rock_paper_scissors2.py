def decode(inp):
    switch = {
        'A': 'rock',
        'X': 'loss',
        'B': 'paper',
        'Y': 'draw',
        'C': 'scissors',
        'Z': 'win'
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
    win_s = 'win'
    draw_s = 'draw'
    loss_s = 'loss'
    if p2 == win_s:
        if p1 == rock_s:
            return (paper_s, win+paper)
        if p1 == paper_s:
            return (scissors_s, win+scissors)
        if p1 == scissors_s:
            return (rock_s, win+rock)
    if p2 == draw_s:
        if p1 == paper_s:
            return (paper_s, draw+paper)
        if p1 == rock_s:
            return (rock_s, draw+rock)
        if p1 == scissors_s:
            return (scissors_s, draw+scissors)
    if p2 == loss_s:
        if p1 == scissors_s:
            return (paper_s, loss+paper)
        if p1 == paper_s:
            return (rock_s, loss+rock)
        if p1 == rock_s:
            return (scissors_s, loss+scissors)


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
