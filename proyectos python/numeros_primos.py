def esPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumaDivisores(num):
    suma = 0
    for i in range(1, num + 1):
        if num % i == 0 and esPrimo(i):
            suma += i
    return suma
print("\nAutores: Sofia Burbano - Juan Cuatindioy")
print("Hola! Bienvenido al algoritmo que realiza sumas de numeros primos :)")
print("----------------------------------------------------------------------")
numero = int(input("Ingrese un número que desees sumar: "))
print("La sumatoria de los divisores primos del numero que digito es: ", sumaDivisores(numero), "NUMEROS")