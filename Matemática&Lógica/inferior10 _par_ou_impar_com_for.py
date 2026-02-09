num1=int(input("Insira um número inteiro: "))
num2=int(input("Insira um número inteiro: "))
num3=int(input("Insira um número inteiro: "))
num4=int(input("Insira um número inteiro: "))


for i in range(1,5,1):
    
    resto = i % 2

    if (resto==0)and i>10:
        print("o número",i,"é de valor par e superior a dez")

    if (resto!=0) and i<10:
        print("O número",i,"é de valor ímpar e inferior a dez")
