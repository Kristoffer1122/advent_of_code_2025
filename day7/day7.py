input = open("input.txt", "r"). read().strip().split("\n")

# start pos
start_col = 0
for i, char in enumerate(input[0]):
    if char == 'S':
        start_col = i
        break

height = len(input)
width = len(input[0])

# track timelines
timelines = {start_col: 1}

for row in range(height):
    new_timelines = {}

    for col, count in timelines.items():
        if input[row][col] == '^':
            # left
            if col - 1 >= 0:
                new_timelines[col - 1] = new_timelines.get(col - 1, 0) + count

            #right
            if col + 1 < width:
                new_timelines[col + 1] = new_timelines.get(col + 1, 0) + count
        else:
            new_timelines[col] = new_timelines.get(col, 0) + count

    timelines = new_timelines

print(sum(timelines.values()))
