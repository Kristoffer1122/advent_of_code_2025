input = open("input.txt").read().strip().split("\n")

instructions = []
working = []
ranges = []

for num, ingredient in enumerate(input):
    if ingredient == "":
        instructions = input[:num]
        working = input[num + 1:]
        break

# filter ranges
for instruction in instructions:
    range_parts = instruction.split("-")
    if len(range_parts) == 2:
        ranges.append((int(range_parts[0]), int(range_parts[1])))

# check each ingredient
fresh_count = 0
for ingredient_id in working:
    ingredient_id = int(ingredient_id)
    is_fresh = False

    # check if ingredient in ranges
    for range_start, range_end in ranges:
        if range_start <= ingredient_id <= range_end:
            is_fresh = True
            break

    if is_fresh:
        fresh_count += 1

print(f"\nTotal fresh ingredients: {fresh_count}")
