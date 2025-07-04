import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa a variável para armazenar a tentativa do usuário
tentativa = 0

print("Bem-vindo ao jogo de adivinhação!")

# Loop enquanto o usuário não acertar o número
while True:
    # Solicita ao usuário para adivinhar o número
    palpite = int(input("Digite um número entre 1 e 100: "))
    
    # Incrementa o número de tentativas
    tentativa += 1
    
    # Verifica se o palpite é igual ao número secreto
    if palpite == numero_secreto:
        print("Parabéns, você acertou em ", tentativa, "tentativas!")
        break
    else:
        # Fornece dicas se o palpite foi alto ou baixo
        if palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")