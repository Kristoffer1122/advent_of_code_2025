input = open("input.txt", "r"). read(). strip().split("\n")

# all lines same width
width = max(len(line) for line in input)
input = [line.ljust(width) for line in input]

problems = []
col = width - 1

# read right to left
while col >= 0:
    if all(row[col] == ' ' for row in input):
        col -= 1
        continue

    # find operand start and end
    problem_end = col
    while col >= 0 and any(row[col] != ' ' for row in input):
        col -= 1
    problem_start = col + 1

    numbers = []
    operator = None

    # read each column right to left
    for c in range(problem_end, problem_start - 1, -1):
        digits = []
        for row in input:
            if row[c] in ['+', '*']:
                operator = row[c]
            elif row[c] != ' ':
                digits. append(row[c])

        if digits:
            numbers.append(int(''.join(digits)))

    # find result
    result = numbers[0]
    for num in numbers[1:]:
        result = result + num if operator == '+' else result * num

    problems.append(result)

print(sum(problems))
