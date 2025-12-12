num1=int(input("Insira um número inteiro: "))
num2=int(input("Insira um número inteiro: "))
num3=int(input("Insira um número inteiro: "))
num4=int(input("Insira um número inteiro: "))

resto1 = num1 % 2
if (resto1==0)and num1>10:
    print("o número",num1,"é de valor par e superior a dez")

if (resto1!=0) and num1<10:
    print("O número",num1,"é de valor ímpar e inferior a dez")

resto2 = num2 % 2
if (resto2==0)and num2>10:
    print("O número",num2,"é de valor par e superior a dez")

if (resto2!=0) and num2<10:
    print("O número",num2,"é de valor ímpar e inferior a dez")

resto3 = num3 % 2
if (resto3==0)and num3>10:
    print("O número",num3,"é de valor par e superior a dez")

if (resto3!=0) and num3<10:
    print("O número",num3,"é de valor ímpar e inferior a dez")

resto4 = num4 % 2
if (resto4==0)and num4>10:
    print("O número",num4,"é de valor par e superior a dez")

if (resto4!=0) and num4<10:
    print("O número",num4," é de valor ímpar e inferior a dez")


