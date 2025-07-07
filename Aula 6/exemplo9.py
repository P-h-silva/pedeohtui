listaDuplicatas = [1,2,3,1,4,2,5,6,3,7,8,5,9]
listaSemDuplicatas = []

while listaDuplicatas:
    elemento = listaDuplicatas.pop(0)
    if elemento not in listaSemDuplicatas:
        listaSemDuplicatas.append(elemento)

print ("Lista sem repetição", listaSemDuplicatas)