import itertools

osumat = {} #key = x, value 
f = open("input.txt", "r")
intxt = f.read()
f.close()

intxt = list(intxt.strip().split("\n"))
kord = [[[int(k) for k in j.split(",")] for j in i.split(" -> ")] for i in intxt]
validitKord = [x for x in kord if x[0][0] == x[1][0] or x[0][1] == x[1][1]]

#x[0] on x 
def laske(kordinaatit : list):
    for x in kordinaatit:
        xyla = max(x[0][0],x[1][0])
        xala = min(x[0][0],x[1][0])
        yyla = max(x[0][1],x[1][1])
        yala = min(x[0][1],x[1][1])
        #tehdään listat
        if x[0][0] > x[1][0]:
            xli = [x for x in range(xala, xyla+1)]
        else: 
            xli = [x for x in range(xyla, xala-1, -1)]
        if x[0][1] > x[1][1]:
            yli = [y for y in range(yala, yyla+1)]
        else: 
            yli = [y for y in range(yyla, yala-1, -1)]
        
        if x[0][0] == x[1][0]: 
            os = [(xala,y) for y in yli]
        elif x[0][1] == x[1][1]:
            os = [(x,yyla) for x in xli]
        else: #vino
            os =  list(zip(xli, yli))

        for k in os:
            try:
                osumat[k] += 1
            except Exception as e:
                osumat[k] = 1
    return osumat.values()
        

lista = laske(kord)
tulos = [x for x in lista if x > 1]
print(len(tulos))
