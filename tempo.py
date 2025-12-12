seg = int(input("Valor dos segundos: "))
min = int(input("Valor dos minutos: "))
h= int(input("Valor das horas: "))

if (seg<60) and (seg>=0) and (min<60) and (min>=0) and (h>=0):
    
    res= int(seg + min*60 + h*3600)
    print("O valor de segundos é de: ",res)  
    
else:
    print("Valor introduzido inválido")
