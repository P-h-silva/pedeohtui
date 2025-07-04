numero = int (input("Digite um numero"))
contador = 1
while contador <=10:
    print (numero, "x", contador, "=", numero*contador)
    contador += 1
print ("Fim do exemplo 1")

contador = 1
while contador <=10:
    print (f"{numero} x {contador} = {numero * contador}")
    contador = contador + 1
print ("Fim do exemplo 2")