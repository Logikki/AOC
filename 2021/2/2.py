depth = 0
horiz = 0
aim = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n","")
        if "forward" in line:
            amount = int((line.replace("forward", "")))
            horiz += amount
            depth += aim*amount
        elif "down" in line:
            amount = int((line.replace("down", "")))
            aim += amount
        elif "up" in line:
            amount = int((line.replace("up", "")))
            aim -= amount
print(depth*horiz)
            