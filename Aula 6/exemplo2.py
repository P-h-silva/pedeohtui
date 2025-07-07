minha_lista = [1,2,3,4,5,6,7,8,9,10]
for i in range (len(minha_lista)):
    print ("O elemento", i+1, "da lista é: ", minha_lista[i])

    print ("------------")
    for i in minha_lista:
        print (i, " - com for")
    
    print ("--------")
    i = 0
    while i<len(minha_lista):
        print (i, " - com while")
        i +=1