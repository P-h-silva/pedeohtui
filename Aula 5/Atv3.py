soma = 0
print ("Digite uma sequencia de numeros inteiros. Digite um numero negativo para encerra.")
while True:
    numero = int(input("Digite um numero:"))
    if numero < 0:
        break
    soma += numero
print ("A soma dos numeros digitados é:", soma)