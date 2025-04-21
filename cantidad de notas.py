# cantidad=int(input("Ingrese cantidad de notas:"))

# suma=0

# for i in range(cantidad):
#     print("Ingrese nota", i+1)
#     nota=float(input())
#     # suma+=nota -> es igual a la linea 7
#     suma=suma+nota

# prom=suma/cantidad

# print("El promedio de notas es ", prom)

cant_alum=int(input("Ingrese cantidad de alumnos:"))

for j in range (cant_alum):
    print("Ingrese numero de notas del alumno", j+1)
    cant_notas=int(input())
    suma=0
    for i in range(cant_notas):
        print("Ingrese nota", i+1, "del alumno", j+1)
        nota=float(input())
        suma+=nota

    prom=suma/cant_notas

    print("El promedio de notas del alumno", j+1, "es", prom)
    if prom>4:
        print("El alumno", j+1, "está aprobado")
    else:
        print("El alumno", j+1, "está reprobado")