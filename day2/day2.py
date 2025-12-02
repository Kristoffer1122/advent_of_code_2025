input = open("./input.txt", "r").read().strip()

pos = 0
sum = 0

for line in input.split(","):
    newline = line. split("-")

    for id in range(int(newline[0]), int(newline[1])+1):
        strid = str(id)
        lenid = len(strid)

        # try all possible pattern lengths
        for patternlen in range(1, int(lenid/2)+1):

            # check if length is divisible by pattern length
            if lenid % patternlen == 0:
                pattern = strid[0:patternlen]
                repetitions = int(lenid / patternlen)

                print("\n",pattern, "repeated", repetitions, "times")

                # check if pattern repeated makes the full id
                if pattern * repetitions == strid:
                    print("invalid id:", strid)
                    sum += id
                    break

print("sum:",sum)
