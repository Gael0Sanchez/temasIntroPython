import os 

def funcion1():
    os.system("cls")
    print("Suma")
    print("ingresa dos numeros")
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print("el resultado es: ", num1 + num2) 
    print("Menu de opc")
    print("1.- Suma")
    print("2.- SumResta")
    print("3.- SumResta")
    print("4.- SumResta")
    print("5.- Salir")
    opc = int(input("Elige una opcion: "))
    if opc == 1:
        funcion1()
    if opc == 2:
        funcion2()
    if opc == 3:
        funcion3()
    if opc == 4:
        funcion4()


def funcion2():
    os.system("cls")
    print("Resta") 
    print("ingresa dos numeros")
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print("el resultado es: ", num1 - num2) 
    print("Menu de opc")
    print("1.- Suma")
    print("2.- SumResta")
    print("3.- SumResta")
    print("4.- SumResta")
    print("5.- Salir")
    opc = int(input("Elige una opcion: "))
    if opc == 1:
        funcion1()
    if opc == 2:
        funcion2()
    if opc == 3:
        funcion3()
    if opc == 4:
        funcion4()

def funcion3():
    os.system("cls")
    print("Multiplicacion") 
    print("ingresa dos numeros")
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print("el resultado es: ", num1 * num2) 
    print("Menu de opc")
    print("1.- Suma")
    print("2.- SumResta")
    print("3.- SumResta")
    print("4.- SumResta")
    print("5.- Salir")
    opc = int(input("Elige una opcion: "))
    if opc == 1:
        funcion1()
    if opc == 2:
        funcion2()
    if opc == 3:
        funcion3()
    if opc == 4:
        funcion4()

def funcion4():
    os.system("cls")
    print("Division") 
    print("ingresa dos numeros")
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print("el resultado es: ", num1 / num2) 
    print("Menu de opc")
    print("1.- Suma")
    print("2.- SumResta")
    print("3.- SumResta")
    print("4.- SumResta")
    print("5.- Salir")


def run():
    os.system("cls")
    print("Menu de opc")
    print("1.- Suma")
    print("2.- SumResta")
    print("3.- SumResta")
    print("4.- SumResta")
    print("5.- Salir")
    opc = int(input("Elige una opcion: "))
    if opc == 1:
        funcion1()
    if opc == 2:
        funcion2()
    if opc == 3:
        funcion3()
    if opc == 4:
        funcion4()

if __name__ == "__main__":
        run()