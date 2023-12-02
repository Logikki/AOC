f = open("input.txt", "r") 
fr = f.read()
f.close()

kalat = [int(x) for x in fr if x != ","]
def eka(kalat : list):
    for p in range(80):
        for i in range(len(kalat)):
            if kalat[i] == 0:
                kalat[i] = 6
                kalat.append(8)
            else: 
                kalat[i] -= 1
    print(len(kalat))

dict_kala = {}

for i in range(9):
    dict_kala[i] = 0

for kala in kalat:
    try:
        dict_kala[kala] += 1
    except:
        dict_kala[kala] = 1

def update_dict(dict):
    apu_dict = {}
    apu_dict[6] = dict[0] + dict[7]
    apu_dict[7] = dict[8]
    apu_dict[8] = dict[0]
    for i in range(1,7):
        apu_dict[i-1] = dict[i]
    return apu_dict


print(dict_kala)

for i in range(256):
    dict_kala = update_dict(dict_kala)
print(sum(dict_kala.values()))