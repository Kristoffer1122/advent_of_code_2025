input = open("input.txt", "r").read().strip()

maxsize = 0
maxx = 0
maxy = 0
positions = []

# get height and width
for line in input.split("\n"):
    x, y = line.split(",")
    positions.append([int(x), int(y)])
    if int(x) > maxx:
        maxx = int(x)
    if int(y) > maxy:
        maxy = int(y)

for pos, val in enumerate(positions):
    for check in positions:
        nowx = abs((val[0]+1) - check[0])
        nowy = abs((val[1]+1)- check[1])
        thissize = nowx * nowy

        if thissize > maxsize:
            maxsize = thissize

        print("max? between", val, check, "height",nowy, nowx , thissize)

        continue

print("Max area:", maxsize)
