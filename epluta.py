def main():
    golpes = [-6,1,-10,-5,8,-15,-10,-5,-6]
    vidaKen = 50
    vidaRyu = 50
    i = 0
    vitoriaRyu = 0
    vitoriaKen = 0
    acuGolpes = 0
    tamanhoGolpes = count(golpes)
    while(i<tamanhoGolpes):
        if(golpes[i] < 0):
            while(golpes[i] < 0):
                acuGolpes += golpes[i]
            vidaRyu += acuGolpes
            acuGolpes = 0
        else:
            while(golpes[i] > 0):
                acuGolpes += golpes[i]
            vidaKen -= acuGolpes
            acuGolpes = 0
        if(vidaKen < 1):
            vidaKen = 50
            vidaRyu = 50
            vitoriaRyu += 1
        else:
            vidaKen = 50
            vidaRyu = 50
            vitoriaKen += 1
    if(vitoriaKen > vitoriaRyu):
        print("Ken ganhou!")
    elif(vitoriaKen == vitoriaRyu):
        print("Empatou!")
    else:
        print("Ryu ganhou!")

