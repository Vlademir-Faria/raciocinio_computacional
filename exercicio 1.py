def calcular_fatorial(num):
    fatorial = 1
    for i in range(num, 0, -1):
        fatorial *= i
        expressao += str(i)
        if i > 1:
            expressao += "*"
    return fatorial, expressao
 
num = int(input("Digite um número para calcular a fatorial: "))
print(f"O valor da fatorial de {num} é {calcular_fatorial(num)}.")