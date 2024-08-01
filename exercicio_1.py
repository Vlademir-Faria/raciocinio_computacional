nums = []
# Coleta os números do usuário
for i in range(6):
    num = int(input("Digite um número: "))
    nums.append(num)

# calcula a soma e a média dos números
soma = sum(nums)
media = soma / len(nums)

print(f"A média final foi {media:.1f}")

# cria listas para armazenar números iguais ou acima da média e números abaixo da média
maior_media = []
menor_media = []

# Separa os números nas respectivas listas e imprime mensagens
for num in nums:
    if num >= media:
        maior_media.append(num)
    else:
        menor_media.append(num)

# imprime as listas finais
print("Números iguais ou acima da média:", maior_media)
print("Números abaixo da média:", menor_media)