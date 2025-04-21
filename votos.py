
votantes=int(input("¿Cuantos votantes son?"))
rafa=0
leo=0
for i in range(votantes):
    print("Elija candidato: rafa (1) / leo (2)")
    opcion=int(input())
    if opcion==1:
        rafa=rafa+1
    elif opcion==2:
        leo=leo+1
    else:
        print("Opción inválida (1 o 2)")

if rafa > leo:
    print("Gana Rafa con", rafa, "votos")
else:
    print("Gana Leo con", leo, "votos")
    
