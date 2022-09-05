with open("input.txt", "r") as f:
    inp = f.read()
paikat = list(map(int, inp.split(",")))

loydettyMin : int

def gas(paikat : list, paikka : int):
    gasoline = 0
    for val in paikat:
        gasoline += max(val, paikka) - min(val, paikka)
    return gasoline

def gas2(paikat : list, paikka : int):
    gasoline = 0
    for val in paikat:
        a = 1
        b = max(val, paikka) - min(val, paikka)
        n = b        
        gasoline += n*(a+b)/2 #aritmeettinen summa
    return(gasoline)

for i in range(max(paikat) + 1 ):
    apu = gas2(paikat, i)
    try:
        loydettyMin = min(loydettyMin, apu)
    except:
        loydettyMin = apu

print(loydettyMin)