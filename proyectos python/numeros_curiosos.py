def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def numeros_curiosos(n):
    curiosos = []
    i = 1
    while len(curiosos) < n:
        if i == suma_divisores(i):
            curiosos.append(i)
        i += 1
    return curiosos
print("\nAutores: Sofia Burbano - Juan Cuatindioy")
print("\nHola! Bienvenido al algoritmo de numeros curiosos :)")
print("----------------------------------------------------------------------")
n = int(input("Ingrese la cantidad de números curiosos que desea calcular: "))
print("Los primeros", n, "números curiosos que usted desea calcular son:", numeros_curiosos(n))