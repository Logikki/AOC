with open("input.txt", "r") as f:
    listat = []
    intxt = f.read()

intxt = list(intxt.strip().split("\n"))
listatut = [[int(x) for x in li] for li in intxt]

def eka(listatut):
    s = 0
    for i in range(len(listatut[0])):
        s += min([x[i] for x in listatut]) + 1
    return s
print(eka(listatut))