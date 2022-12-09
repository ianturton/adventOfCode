from collections import Counter

len_marker = 14
with open('input') as f:
    line = f.readline().strip()
    for i in range(len(line)):
        mark = line[i: i+len_marker]
        counts = Counter(mark)
        print(mark, counts)
        uniq = True
        for count in counts.values():
            if count > 1:
                uniq = False

        if uniq:
            print(i+len_marker, line[:i+len_marker+1])
            break
