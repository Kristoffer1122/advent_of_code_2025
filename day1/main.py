inputpass = open("input.txt", "r").read(). strip()

def solve():

    tick = 50
    password = 0

    for line in inputpass. split("\n"):

        count = line[1:]

        if len(count) > 2:
            password += int(count) // 100

        turs = (int(line[1:]) % 100)

        if line[0] == "L":
            if tick > 0 and tick < turs:
                password += 1
            tick -= turs

        elif line[0] == "R":
            if tick + turs > 100:
                password += 1
            tick += turs

        tick = tick % 100

        if tick == 0:
            password += 1 

    print(password)

solve()
