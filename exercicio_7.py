media = 0
soma = 0
num = -1
contador = 0
while True:
    num = int(input("Digite um número pra fazer a média (0 pra finalizar): "))
    soma += num
    contador += 1
    if num == 0:
        break
    media = soma / contador
print("A média é ", media)