lista = [17,8,10,6,2,4]
trocado = True
while trocado:
    trocado = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            trocado = True
            lista[i], lista[i+1] = \
                 lista[i+1], lista[i]
            
print(lista)