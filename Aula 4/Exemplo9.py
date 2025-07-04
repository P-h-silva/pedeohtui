tentativas = 0
while tentativas < 3:
    senha = input ("Digite a senha")
    if senha == "senha123":
        print ("Acesso concedido!")
        break
    else:
        print ("Ssenha Incorreta! Tenta novamente!")
        tentativas += 1
else:
    print ("Você excedeu o numero de tentativas.")