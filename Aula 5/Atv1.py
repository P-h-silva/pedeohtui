# Solicita ao usuário um valor entre 1 e 10
valor = int(input("Digite um valor entre 1 e 10: "))
# Verifica se o valor está no intervalo válido
if 1 <= valor <= 10:
    # Imprime a tabuada de 1 a 10 para o valor informado
    print(f"\nTabuada de {valor}:\n")
    for i in range(1, 11):
        resultado = valor * i
        print(valor, "x" ,i, "=", resultado)
else:
    print("Por favor, digite um valor entre 1 e 10.")