numero = int (input("Entre com um numero positivo:"))
for i in range(2, numero):
    if numero % i == 0:
        print (numero, "não é um numero primo.")
        break
else:
    print (numero, "é um numero primo.")