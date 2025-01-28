import os
from io import open

class Diccionario:

    pEsp = 0 
    pEng = 0

    def _init_(self, a, b):
        self.p = a
        self.pEng = b

    def agregarP(self):
        
        print("Escribe una palabra en español:")
        self.pEsp = input("Palabra en español: ")
        print("Escribe la traduccion:")
        self.pEng = input("Palabra en ingles: ")
        archivo = open("dicc.txt", "a")
    
        archivo.write(self.pEsp)
        archivo.write(" ")
        archivo.write(self.pEng)
        archivo.write("\n")
        archivo.close()
        print("Se agrego la nueva palabra {} al diccionario".format(self.pEsp))
        input("¿Deasea continuar? presione enter")


    def buscarPalbraTrad(self):

        texto = ""

        print("Elige en que idioma quieres traducir")
        print("1.- Español")
        print("2.- Ingles")
        opcion = int(input("Selecciones una opcion: "))

        if opcion == 1:
            print("Escribe la palabra en español: ")
            self.pEsp = input("Palabra en español: ")

        if opcion == 2:
            print("Escribe la palabra en ingles: ")
            self.pEng = input("Palabra en ingles: ")

        archivo = open("dicc.txt","r")

        for line in archivo:
            texto += line
        archivo.close()

        print(texto)

        if self.pEsp in texto:
            print("la palabra {} se ha encontrado en el diccionario".format(self.pEsp))
            input("Si desea regresar al menu presione enter")
        else:
            print("La palbara no se encontro")
            input("Si desea agregar la nueva palabra presione enter")

        if self.pEng in texto:
            print("la palabra {} se ha encontrado en el diccionario".format(self.pEng))
            input("Si desea regresar al menu presione enter")
        else:
            print("la palabra no se encontro")
            input("Si desea agregar la nueva palabra presione enter")

def run():  
    dic = Diccionario()
    while True:
        os.system('cls')
        print("Menu de opciones:")
        print("1.- Agregar palabra")
        print("2.- Buscar palabra")
        print("3.- Salir")

        opc = int(input("Elige una opcion: "))

        if opc == 1:
            dic.agregarP()
        if opc == 2:
            dic.buscarPalbraTrad()
        if opc == 3:

            break

if __name__ == "__main__":
    run()