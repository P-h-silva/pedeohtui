tipo = input("Digite p para par e i para ímpar:")
for i in range (0, 1000):
    if tipo == "p" and i % 2 == 0:
        print (i, end="-")
    elif tipo == "i" and i % 2 != 0:
        print (i, end="-")