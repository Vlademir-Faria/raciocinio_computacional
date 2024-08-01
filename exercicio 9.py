valor_saque = int(input("Digite o valor que deseja sacar: R$"))
resto = valor_saque
n1 = n2 = n5 = n10 = n20 = n50 = n100 = n200 = 0

if valor_saque < 10 or valor_saque > 600:
    print("Valor mínimo de saque: R$ 10,00. Valor máximo de saque: R$ 600,00. Favor digitar outro valor.")
else:
    if resto >= 200:
        sobra = resto % 200
        n200 = int((resto - sobra) / 200)
        resto = sobra
    if resto >= 100:
        sobra = resto % 100
        n100 = int((resto - sobra) / 100)
        resto = sobra
    if resto >= 50:
        sobra = resto % 50
        n50 = int((resto - sobra) / 50)
        resto = sobra
    if resto >= 20:
        sobra = resto % 20
        n20 = int((resto - sobra) / 20)
        resto = sobra
    if resto >= 10:
        sobra = resto % 10
        n10 = int((resto - sobra) / 10)
        resto = sobra
    if resto >= 5:
        sobra = resto % 5
        n5 = int((resto - sobra) / 5)
        resto = sobra
    if resto >= 2:
        sobra = resto % 2
        n2 = int((resto - sobra) / 2)
        resto = sobra
    n1 = resto
    print("Notas de R$200,00", n200)
    print("Notas de R$100,00", n100)
    print("Notas de R$50,00", n50)
    print("Notas de R$20,00", n20)
    print("Notas de R$10,00", n10)
    print("Notas de R$5,00", n5)
    print("Notas de R$2,00", n2)
    print("Notas de R$1,00", n1)