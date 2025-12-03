input = open("./input.txt", "r"). read(). strip()

total = 0

for line in input.split('\n'):
    n = len(line)

    result = []

    for i in range(n):
        while result and result[-1] < line[i] and len(result) + (n - i) > 12:
            result.pop()
        if len(result) < 12:
            result.append(line[i])

    total += int(''.join(result))

print(total)
