
from collections import defaultdict
from pathlib import Path


class TreeNode:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.children = set()
        self.size = 0

    def printChildren(self, indent=0):
        for child in self.children:
            child.printChildren(indent + 1)

    def getChildren(self, data):
        print(self.data, self.size)
        for child in self.children:
            child.getChildren(data)
        if self.children:
            print(self.data, "storing ", self.getSize())
            data[self.data] = self.getSize()
        return

    def getSize(self):
        size = self.size
        for child in self.children:
            size += child.getSize()
            print("**", child.data, size)
        return size

    def __repr__(self):
        ret = f'{self.data}:({self.size})->{[c for c in self.children]}'
        return ret


root = TreeNode('/', None)
current = root


def process_commands(f):
    global root
    global current

    while True:
        line = f.readline().strip()
        if not line:
            break

        if line.startswith('$ '):
            input = line[2:]
            if input.startswith('ls'):
                # read until next line with $
                while True:
                    line = f.readline().strip()
                    if not line:
                        break
                    if line.startswith('$'):
                        input = line[2:]
                        break

                    parts = line.split()
                    if parts[0] != 'dir':
                        node = TreeNode(parts[1], current)
                        current.children.add(node)
                        node.size = int(parts[0])

            if input.startswith('cd'):
                # change directory
                if input[3:].startswith('/'):
                    current = root
                elif input[3:].startswith('..'):
                    current = current.parent
                    if not current:
                        raise RuntimeError("tried to move above root")
                else:
                    child = TreeNode(input[3:], current)
                    current.children.add(child)
                    current = child


def process(data):
    current_folder = Path()
    file_sizes = {}
    for line in data:
        match line.split():
            case ['$', 'cd', folder]:
                current_folder = current_folder.joinpath(folder) \
                    .resolve(strict=False)
            case ['$', 'ls']:
                pass
            case ['dir', _]:
                pass
            case [size, file]:
                file_sizes[current_folder / file] = int(size)
            case _:
                return 'nope'

    folder_sizes = defaultdict(int)
    for file, size in file_sizes.items():
        for p in file.parents:
            folder_sizes[p] += size

    return folder_sizes


def part_one(data):
    folder_sizes = process(data)
    return sum(s for s in folder_sizes.values() if s <= 100000)


def part_two(data):
    folder_sizes = process(data)
    root_size = folder_sizes.get(Path('/'))
    print("root", root_size)
    free_space = 70000000 - root_size
    print("free", free_space)
    target = 30000000 - free_space
    print("target", target)
    for folder, size in sorted(folder_sizes.items(), key=lambda a: a[1]):
        if size >= target:
            print(size, folder)
            break


with open('input') as f:
    print(part_two(f.readlines()))


# root.printChildren()
# results = {}
# root.getChildren(results)
#
# sum = 0
# for k, v in results.items():
#     if v <= 100000:
#         print(k, v)
#         sum += v
#
#
# print(sum)
