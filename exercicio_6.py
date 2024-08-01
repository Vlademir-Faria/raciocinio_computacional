import getpass
while True:
    login = input("Digite seu login: ")
    senha = getpass.getpass("Digite sua senha: ")
    if login != senha:
        print("Bem-vindo ao sistema!")
        break
    else:
        print("Login e senha iguais. Favor digitar informações diferentes!")