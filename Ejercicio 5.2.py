# Ejercicio 5.2:("Definir una funcion que acepte tres valores y delvuelva el maximo de los tres")

n1 =float(input("ingrese el primer valor"))
n2 =float(input("ingrese el segundo valor"))
n3 =float(input("ingrese el tercer valor"))


def mayor(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print("El mayor es: ",n1)

    if n2 > n1 and n2 > n3:
    print("El mayor es: ", n2)

    if n3 > n1 and n3 > n2:
    print("El mayor es: ", n3)


mayor(n1,n2,n3)


