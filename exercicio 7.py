triangulo = print("Informe os valores dos lados do triângulo:")
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado3 + lado1 < lado2:
    print("Esse é um triângulo triângulo!")
else:
    if lado1 == lado2 and lado1 == lado3:
        print("Esse é um triângulo equilátero!")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("Esse é um triângulo isóseles!")
    else:
        print("Esse é um escaleno!")