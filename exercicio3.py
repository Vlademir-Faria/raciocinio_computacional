print("Por favor, insira três números diferentes:")
num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
num3 = float(input("digite o terceiro número: "))

# Verificando se os números são diferentes
if num1 == num2:
    print("Os números inseridos não são diferentes.")
else:
    if num1 == num3:
        print("Os números insridos não são diferentes.")
    else:
        if num2 == num3:
            print("Os números inseridos não são diferenetes.")
        else:
            menor = num1

            if num2 < menor:
                menor = num2
            
            if num3 < menor:
                menor = num3
            
            print(f"O menor número é {menor}")