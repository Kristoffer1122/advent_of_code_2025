input = open("input.txt", "r"). read().strip().split("\n")

# start pos
start_col = 0
for i, char in enumerate(input[0]):
    if char == 'S':
        start_col = i
        break

height = len(input)
width = len(input[0])

# active beams
beams = set()
beams.add(start_col)

splits = 0

# process row by row
for row in range(1, height):
    new_beams = set()

    for col in beams:
        if input[row][col] == '^':
            # split beam
            splits += 1

            # add left beam
            if col - 1 >= 0:
                new_beams.add(col - 1)

            # add right beam
            if col + 1 < width:
                new_beams.add(col + 1)
        else:
            # continue straight down
            new_beams.add(col)

    beams = new_beams

print(splits)
