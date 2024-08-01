nota1 = float(input("Coloque a nota do primeiro bimestre: "))
nota2 = float(input("Coloque a nota do segundo bimestre: "))
nota3 = float(input("Coloque a nota do terceiro bimestre: "))
nota4 = float(input("Coloque a nota do quarto bimestre: "))
pres1 = int(input("Coloque o número de falta em aula no primeiro bimestre: "))
pres2 = int(input("Coloque o número de falta em aula no segundo bimestre: "))
pres3 = int(input("Coloque o número de faltas no terceiro bimestre: "))
pres4 = int(input("Coloque o número de faltas no quarto bimestre: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
pres = (pres1 + pres2 + pres3 + pres4) / 4
media_pres = 100 - (pres * 100) / 40

if media >= 7 and media_pres >= 75:
    print(f"Sua média final é {media} e sua média de presença foi {media_pres}% e você foi APROVADO!")
else:
    print(f"Sua média final é {media} e sua média de presença foi {media_pres}% e infelizmente você foi REPROVADO.")