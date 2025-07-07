banda = []
print ("Etapa 1", banda)
banda.append("John Lennon")
banda.append("Paul McCartney")
banda.append("George Harrison")
print("Etapa 2", banda)
for membros in range (2):
    banda.append(input("Novo membro"))
print ("Etapa 3", banda)
del banda[-1]
del banda[-1]
print("Etapa 4", banda)
banda.insert(0, "Ringostarr")
print("The Beatles:", banda, "\nCom", len(banda), "membros")