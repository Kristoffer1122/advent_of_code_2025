input = open("input.txt").read().strip().split("\n")

instructions = []
ranges = []

for num, ingredient in enumerate(input):
    if ingredient == "":
        instructions = input[:num]
        break

# filter ranges
for instruction in instructions:
    range_parts = instruction.split("-")
    if len(range_parts) == 2:
        ranges.append((int(range_parts[0]), int(range_parts[1])))

# sort ranges by start
ranges.sort()

# merge simmilar ranges
merged = []
for range_start, range_end in ranges:
    if merged and range_start <= merged[-1][1] + 1:
        # simmilar range merge
        merged[-1] = (merged[-1][0], max(merged[-1][1], range_end))
    else:
        merged.append((range_start, range_end))

total = 0
for range_start, range_end in merged:
    total += (range_end - range_start + 1)

print(total)
