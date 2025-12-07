input = open("input.txt", "r"). read(). strip().split("\n")

# all lines same width
width = max(len(line) for line in input)
input = [line.ljust(width) for line in input]

problems = []
col = 0

while col < width:
    if all(row[col] == ' ' for row in input):
        col += 1
        continue

    # find operand start and end 
    problem_start = col
    while col < width and any(row[col] != ' ' for row in input):
        col += 1

    numbers = []
    operator = None

    for row in input:
        value = row[problem_start:col]. strip()
        if value in ['+', '*']:
            operator = value
        elif value:
            numbers.append(int(value))

    # find result
    result = numbers[0]
    for num in numbers[1:]:
        result = result + num if operator == '+' else result * num

    problems.append(result)

print(sum(problems))
