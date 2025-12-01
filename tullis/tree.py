import random

star = "\033[1;38;2;255;223;0m67\033[0m"

max = 20
for x in range(max):
    if x == 1:
        print(" "*(max-x),star.center(max))
    else:
        # random indivudual ones should be colored differently
        print(" "*(max-x),("\033[32m67"*x).center(max//5))



        # color = f"\033[38;2;0;{random.randint(100,255)};0m"
        # print(" "*(max-x), (color + "67"*x + "\033[0m").center(max))


print(" "*max,("\033[38;2;101;67;33m|||\033[0m"))
print(" "*max,("\033[38;2;101;67;33m|||\033[0m"))
print(" "*max,("\033[38;2;101;67;33m|||\033[0m"))

