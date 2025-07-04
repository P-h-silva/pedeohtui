import random

# Inicializa as variáveis para contar o número de caras e coroas
num_caras = 0
num_coroas = 0

# Solicita ao usuário o número de vezes que deseja jogar a moeda
num_jogadas = int(input("Digite o número de vezes que deseja jogar a moeda: "))

# Loop para simular o lançamento da moeda e contar caras e coroas
for _ in range(num_jogadas):
    resultado = random.randint(0, 1)
    
    # Verifica o resultado do lançamento e atualiza as contagens
    if resultado == 0:
        print("Cara")
        num_caras += 1
    else:
        print("Coroa")
        num_coroas += 1

# Imprime o número total de caras e coroas
print("\nTotal de caras:", num_caras)
print("Total de coroas:", num_coroas)