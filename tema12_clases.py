class OperasBas: 
    #declaracion de propiedaades

    #privado un guion bajo "_" protegido doble "__" y publico solo declararlo

    num1 = 0
    num2 = 0
    r = 0

    #declaracion de constructor de la clase

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        
    #declaracion de metodos de la clase
    def suma(self):
        self.r = self.num1+self.num2
        print("La suma es: {}".format(self.r))

def main():
    obj = OperasBas(3, 5)
    obj.suma()

if __name__ == "__main__":
    main()
