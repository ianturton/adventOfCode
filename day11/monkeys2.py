import math


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
        return res

    def __repr__(self):
        return f"Monkey {self.number}: Holding: {self.start_items}, {self.op=}"

    def process(self):
        ret = []
        for item in self.start_items:
            score = self.calc_score(item)
            if score % self.test:
                ret.append((self.false, score))
            else:
                ret.append((self.true, score))

        self.start_items = []
        return ret


monkeys = []


with open('input') as f:
    n_monkeys = 8
    lines = f.readlines()
    for i in range(0, n_monkeys * 7, 7):
        monkeys.append(Monkey(lines[i:i + 7]))
        print(monkeys[i // 7])

    # here we collect the lcd of the test values to mod by later
    # see https://aoc.just2good.co.uk/2022/11#part-2
    divisor = math.prod([m.test for m in monkeys])
    for rounds in range(10000):
        for monkey in monkeys:
            targets = monkey.process()
            for i in targets:
                monkeys[i[0]].start_items.append(i[1] % divisor)

    monkeys.sort(key=lambda m: m.inspected, reverse=True)
    print(monkeys[0].inspected * monkeys[1].inspected)
