x = 0
i = 1

print("Ingresa un numero")
x = int(input("x: "))

while i <= 10:
    res = x * i
    print("{} x {} = {}".format(x, i, res))
    i += 1