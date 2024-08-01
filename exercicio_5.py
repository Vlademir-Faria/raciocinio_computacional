print("Calculadora de potências.")
# Função para validar se a entrada é um número inteiro.
def obter_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
# solicitar os números ao usuário
numerador = obter_numero("Digite o numero: ")
expoente = obter_numero("Digite o expoente: ")
# calcular a potência manualmente
resultado = 1
for _ in range(abs(expoente)):
    resultado *= numerador
# ajustar o resultado para expoentes negativos
if expoente < 0:
    resultado = 1 / resultado
print(f"{numerador} elevado a {expoente} é igual a {resultado}")