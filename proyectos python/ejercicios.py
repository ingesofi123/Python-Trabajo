while True:
    print("\nAutores: Sofia Burbano - Juan Cuatindioy")
    print("\nSelecciona una Opcion :)")
    print("1. Lecturas de energia electrica: ")
    print("2. Sumatoria de divisores primos: ")
    print("3. Numeros curiosos ")
    print("4. salir")
    opcion= int(input("Seleccione lo que quiere realizar"))
    if opcion == 1:
        print("\nSelecciona una Opcion :)")
        print("1. Para ingresar una nueva lectura")
        print("2. Para calcular promedio de lecturas")
        print("2. Para calcular promedio de lecturas")
        print("3. Para mostrar lectura máxima")
        print("4. Para mostrar lectura mínima")
        print("5. Para mostrar la cantidad de lecturas realizadas")
        print("6. Para Salir")
        op = int(input("Ingrese la opcion que desea visualizar: "))
        if op == 1:
            print("Usted ah seleccionado la opcion 1 de ingresar una nueva escritura :)")
            print("--------------------------------------------------------------------")
            lectura = float(input("Ingrese la lectura que desee: "))
            lectura.append(lectura)
        elif op == 2:
            print("Usted ah seleccionado la opcion 2 de calcular el promedio de lecturas :)")
            print("--------------------------------------------------------------------")
            promedio = sum(lectura) / len(lectura)
            print("Promedio de lecturas que desee calcular: ", promedio)
        elif op == 3:
            print("Usted ah seleccionado la opcion 3 de mostrar la lectura maxima)")
            print("--------------------------------------------------------------------")
            print("Lectura máxima que usted ingreso es: ", max(lectura))
        elif op == 4:
            print("Usted ah seleccionado la opcion 4 de mostrar la lectura minima)")
            print("--------------------------------------------------------------------")
            print("Lectura mínima que usted ingreso es: ", min(lectura))
        elif op == 5:
            print("Usted ah seleccionado la opcion 5 la cual muestra la cantidad de lecturas realizadas)")
            print("--------------------------------------------------------------------")
            print("Cantidad de lecturas que usted realizo son: ", len(lectura))
        elif op == 6:
            break
        else:
            print("Ups! esa opción es inválida... Por favor, intente de nuevo :) ")
    elif opcion == 2:
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
        print("Hola! Bienvenido al algoritmo que realiza sumas de numeros primos :)")
        print("----------------------------------------------------------------------")
        numero = int(input("Ingrese un número que desees sumar: "))
        print("La sumatoria de los divisores primos del numero que digito es: ", sumaDivisores(numero), "NUMEROS")