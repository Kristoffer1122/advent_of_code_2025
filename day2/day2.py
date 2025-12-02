input = open("./input.txt", "r").read().strip()

pos = 0
sum = 0

# if we find same two strings in range
# find same characters in the range
# add sum of false id

for line in input.split(","):
    newline = line.split("-");
    seen = set()

    for id in range(int(newline[0]), int(newline[1])+1):

        strid = str(id)
        splitid = list(strid)
        lenid = round(len(splitid)/2)
        print(splitid)

        print("\ncomparing:", splitid[0:int(lenid)], "with", splitid[int(lenid):])
        if splitid[0:int(lenid)] == splitid[int(lenid):]:
            print("invalid id:", strid)
            sum += id

print("sum:",sum)

