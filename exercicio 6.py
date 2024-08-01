num1 = int(input("Escolha um número: "))
num2 = int(input("Escolha outro número: "))
equacao = input("Escolha uma equação: ( + - * / ) ")

if equacao == "+":
    soma = num1 + num2
    print(soma)
elif equacao == "*":
    multiplicacao = num1 * num2
    print(multiplicacao)
elif equacao == "/":
    divisao = num1 / num2
    print(divisao)
elif equacao == "-":
    subtracao = num1 - num2
    print(subtracao)
else:
    equacao = "erro"

if equacao == "erro":
    print("Operação inválida!")
else:
    print("Parabéns!")