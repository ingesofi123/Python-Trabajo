lecturas = []

while True:
    print("\nAutores: Sofia Burbano - Juan Cuatindioy")
    print("\nSelecciona una Opcion :)")
    print("1. Para ingresar una nueva lectura")
    print("2. Para calcular promedio de lecturas")
    print("2. Para calcular promedio de lecturas")
    print("3. Para mostrar lectura máxima")
    print("4. Para mostrar lectura mínima")
    print("5. Para mostrar la cantidad de lecturas realizadas")
    print("6. Para Salir")
    opcion = int(input("Ingrese la opcion que desea visualizar: "))

    if opcion == 1:
        print("Usted ha seleccionado la opcion 1: Ingresar una nueva escritura :")
        print("--------------------------------------------------------------------")
        lectura = float(input("Ingrese la lectura que desee: "))
        lecturas.append(lectura)
    elif opcion == 2:
        print("Usted ha seleccionado la opcion 2: Calcular el promedio de lecturas :")
        print("--------------------------------------------------------------------")
        promedio = sum(lecturas) / len(lecturas)
        print("Promedio de lecturas que desee calcular: ", promedio)
    elif opcion == 3:
        print("Usted ha seleccionado la opcion 3 de mostrar la lectura maxima: ")
        print("--------------------------------------------------------------------")
        print("Lectura máxima que usted ingreso es: ", max(lecturas))
    elif opcion == 4:
        print("Usted ha seleccionado la opcion 4: Mostrar la lectura minima: ")
        print("--------------------------------------------------------------------")
        print("Lectura mínima que usted ingreso es: ", min(lecturas))
    elif opcion == 5:
        print("Usted ha seleccionado la opcion 5: Muestra la cantidad de lecturas realizadas: ")
        print("--------------------------------------------------------------------")
        print("Cantidad de lecturas que usted realizo son: ", len(lecturas))
    elif opcion == 6:
        break
    else:
        print("Ups! esa opción es inválida... Por favor, intente de nuevo : ")