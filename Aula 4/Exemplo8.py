import random
numero_secreto = random.randint(1,100)
tentativa = 1
while tentativa <= 3:
    palpite = int(input("Adivinhe o numero"))
    if palpite == numero_secreto:
        print("Parabéns, você acertou")
        break
    else:
        if palpite > numero_secreto:
            print ("O numero é menor que:", palpite)
        else:
            print ("O numero é maior que:", palpite)
    tentativa += 1
if tentativa > 3:
    print ("Suas tentativas acabaram")
    print ("O numero secreto era:", numero_secreto)