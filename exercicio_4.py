print("Descubra a tabuada do número que escolher!")
tabu=int(input("Escolha um número: "))
for count in range(10):
    print("%d * %d = %d" % (tabu, count+1, tabu*(count+1)))