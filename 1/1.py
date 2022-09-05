
def eka():
    lista = []
    times = 0
    times2 = 0
    kolmensummaLista = []
    with open ("1input.txt", "r") as f:
        for line in f: 
            lista.append(int(line))
    for i in range(len(lista)-1):
        if lista[i+1] > lista[i]:
            times += 1
    print("eka: " + str(times))
    for i in range(1, (len(lista)-1)):
        kolmensummaLista.append(lista[i-1] + lista[i] + lista[i+1])
    for i in range(len(kolmensummaLista)-1):
        if kolmensummaLista[i+1] > kolmensummaLista[i]:
            times2 += 1
    print("toka: " + str(times2))

eka()