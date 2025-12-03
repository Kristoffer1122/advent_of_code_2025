input_data = open("./input.txt", "r").read().strip()

total = 0

for bank in input_data.split('\n'):

    maxval = 0

    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):

            # lage parr av h;ygeste tallene
            joltage = int(bank[i] + bank[j])
            maxval = max(maxval, joltage)

    total += maxval

print(total)
