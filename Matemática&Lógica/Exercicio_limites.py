LInf=int(input("Insira o valor do limite inferior: "))
LSup=int(input("Insira o valor do limite superior: "))

if(LInf>LSup):
    print("Os limites, indicados para o intervalo, estão errados")
else:
    while (LInf<=LSup):
        print(LInf)

        LInf=LInf+1
    




