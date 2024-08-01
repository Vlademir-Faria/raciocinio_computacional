total = 0
continuar = True
while continuar:
    # pedir o nome do produto
    while True:
        nome = input("Digite o nome do produto: ")
        if nome:
            break
        else:
            print("Nome do produto não pode estar vazio, favor digitar o nome do produto!")
    # pedir o valor do produto
    while True:
        try:
            valor_produto = float(input("Digite o valor dos produtos: "))
            if valor_produto > 0:
                break
            else:
                print("Digite o valor do produto, devendo ser um número positivo.")
        except ValueError:
            print("Digite um número válido!")
    # pedir a quantidade do produto
    while True:
        try:
            quantidade_produto = int(input("Digite a quantidade que você está comprando: "))
            if quantidade_produto > 0:
                break
            else:
                print("A quantidade deve ser positiva, digite novamente.")
        except ValueError:
            print("Digite um número válido")
    total += valor_produto * quantidade_produto
    resposta = input("Deseja adicionar mais produtos ou deseja finalizar? (adicionar|finalizar)")
    if resposta == "finalizar":
        continuar = False
    print(f"Valor total da compra: R$ {total:.2f}")