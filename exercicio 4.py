salario = float(input("Informe seu salário: "))
abono = 0

if salario <= 5000:
    abono = salario * 0.15
else:
    abono = salario * 0.10

print(f"Valor do seu anono de fim de ano é de: R${abono:.2f}")