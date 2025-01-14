x = 0
i = 1

print("Ingresa un número para generar su tabla de multiplicar")
x = int(input("x: "))

while i <= 10:
    res = x * i
    print(f"{x} x {i} = {res}")
    i += 1


