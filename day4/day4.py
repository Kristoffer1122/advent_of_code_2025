input = open("input.txt", "r"). read().strip().split("\n")

# lister med strenger kan ikke endres lol pyhton
input = [list(line) for line in input]

saveablerolls = 0
count = 0

rounds = 0

# forstett til ingen flere kan fjernes
while True:
    toremove = []
    roundremoved = 0

    # enumerate op??? (hidden tech (crazy style))
    for current, line in enumerate(input):
        last = current - 1 if current - 1 >= 0 else None
        next = current + 1 if current + 1 < len(input) else None

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
                    toremove.append((current, idx))
                    roundremoved += 1

    if roundremoved == 0:
        break

    # reset rullen
    for current, idx in toremove:
        input[current][idx] = "."

    saveablerolls += roundremoved
    rounds += 1

print(saveablerolls)
