valor = 0
limite = int(input("Digite o número final de febobatti: "))
num1 = 0
num2 = 1
febo = "0, 1"

while valor < limite:
    valor = num1 + num2
    if valor < limite:
        num1 = num2
        num2 = valor
        febo += "," + str(valor)
print("Fibonacci", febo)