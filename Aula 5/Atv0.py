#Peça para  o usuário entrar com dois valores (primeiro e último).
#Faça a contagem entre esses números.
#Caso o último for menor que  o primeiro faça a contagem decrescente.
#Caso o último número for maior que o primeiro faça a contagem crescente.

# Solicita ao usuário os valores
primeiro = int(input("Digite o primeiro valor: "))
ultimo = int(input("Digite o último valor: "))

# Verifica e faz a contagem
if primeiro < ultimo:
    for i in range(primeiro, ultimo + 1):
        print(i, end=' ')
else:
    for i in range(primeiro, ultimo - 1, -1):
        print(i, end=' ')