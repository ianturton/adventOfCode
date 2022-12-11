class Monkey():
    def __init__(self, lines):
        self.number = int(lines[0].strip().replace("Monkey ", '')[:-1])
        self.start_items = [int(i) for i in lines[1].strip().replace("Starting items:", '').split(',')]
        self.op = lines[2].strip().replace("Operation: new = ", '').replace('old', '{old}')
        self.test = int(lines[3].strip().replace("Test: divisible by ", ''))
        self.true = int(lines[4].strip().replace("If true: throw to monkey", ''))
        self.false = int(lines[5].strip().replace("If false: throw to monkey", ''))
        self.inspected = 0

    def calc_score(self, item):
        self.inspected += 1
        # print(f"Inspecting {item=} ({self.inspected=})")
        op = self.op.format(old=item)
        res = eval(op)
        res //= 3
        return res

    def __repr__(self):
        return f"Monkey {self.number}: Holding: {self.start_items}, {self.op=}"


def throw_to(orig, dest, item, new_item):
    global monkeys
    # print(orig, dest)
    monkeys[dest].start_items.append(new_item)


monkeys = []


with open('input') as f:
    n_monkeys = 8
    lines = f.readlines()
    for i in range(0, n_monkeys * 7, 7):
        monkeys.append(Monkey(lines[i:i + 7]))
        print(monkeys[i // 7])

    for rounds in range(20):
        # print(f"Round {rounds+1}")
        for monkey in monkeys:
            thrown = 0
            for item in monkey.start_items:
                score = monkey.calc_score(item)
                thrown += 1
                if not score % monkey.test:
                    throw_to(monkey, monkey.true, item, score)
                else:
                    throw_to(monkey, monkey.false, item, score)

            monkey.start_items = monkey.start_items[thrown:]

    max1 = -1
    max2 = -1
    for monkey in monkeys:
        inspected = monkey.inspected
        if inspected > max1:
            max2 = max1
            max1 = inspected
        elif inspected > max2:
            max2 = inspected

    print(max1 * max2)
