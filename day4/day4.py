input = open("input.txt", "r").read().strip().split("\n")

saveablerolls = 0
count = 0

print(input)
for current, line in enumerate(input):
    last = current - 1 if current - 1 >= 0 else None
    next = current + 1 if current + 1 < len(input) else None

    # enumerate op??? (hidden tech (crazy style))
    for idx, char in enumerate(line):
        if char == "@":
            count = 0

            # check all neighbors but not ourselves
            for x in range(idx - 1, idx + 2):
                # last
                if last is not None and 0 <= x < len(input[last]):
                    if input[last][x] == "@":
                        count += 1
                # current
                if 0 <= x < len(input[current]) and x != idx:
                    if input[current][x] == "@":
                        count += 1
                # next
                if next is not None and 0 <= x < len(input[next]):
                    if input[next][x] == "@":
                        count += 1

            if count < 4:
                saveablerolls += 1

print("sum:", saveablerolls)
