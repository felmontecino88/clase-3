# en python todos los indices comienzan en 0

# for i in range(5):
#     print("Repetición", i+1)

# for i in range(1,6):
#     print("Repetición", i)

# num=int(input("Ingrese un numero:"))

# for i in range(num):
#     print("Repeticion numero", i+1)


# tablas de multiplicar

# num=int(input("Ingrese un numero:"))

# # for i in range(1,11):
# #     print(i, " x ", num, " = ", num*i)

# for i in range(10):
#     print(i+1, " x ", num, " = ", num*(i+1))


# todas las tablas del 1 al 10

# for j in range(10):
#     for i in range(10):
#         print(j+1, "x", i+1, "=", (j+1)*(i+1))


# pedir numero y mostrar si son pares o impares hasta ese numero

# num=int(input("Ingrese un numero:"))

# for i in range(1,num+1):
#     if i % 2==0:
#         print("El numero", i, "es par")
#     else:
#         print("El numero", i, "es impar")

# otra forma

cant=int(input("Ingrese cantidad de numeros:"))

for i in range(cant):
    num=int(input("Ingrese numero:"))
    if i % 2==0:
        print("El numero", num, "es par")
    else:
        print("El numero", num, "es impar")
