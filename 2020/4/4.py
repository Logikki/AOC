fh = open("input.txt", mode='r')
itxt = fh.read()
fh.close()

itxt = list(itxt.strip().split("\n\n"))

bingoNumerot = list(map(int, itxt[0].split(',')))
itxt = [i.split('\n') for i in itxt[1:]]

brds = [[[int(k) for k in j.split(' ') if k != ''] for j in i] for i in itxt]

def pisteet(board: list, haku : list, vikaNumero : int):
    pisteet = 0
    brd = [item for sublist in board for item in sublist if item not in haku]
    for luku in brd:
        pisteet += luku
    return pisteet*vikaNumero
    

def bingo(haku : list, brd : list):
    for rivi in brd:
        vaaka = [i for i in rivi if i in haku]
        if len(vaaka) == 5:
            return True
    for i in range(len(brd)):
        pysty = [item[i] for item in brd if item[i] in haku]
        if len(pysty) == 5:
            return True



def etsi(brds: list, srch: list):
    bingoNumerot = []
    voittaneet = []
    for i in range (len(srch)):
        bingoNumerot.append(srch[i])
        for indeksi, bingoLappu in enumerate(brds):
            if bingo(bingoNumerot, bingoLappu):
                if len(voittaneet) == len(brds) - 1 and indeksi not in voittaneet:
                    return pisteet(bingoLappu, bingoNumerot, srch[i])
                elif indeksi not in voittaneet:
                    voittaneet.append(indeksi)
                else: 
                    continue

print(etsi(brds, bingoNumerot))