# 3) Ingresar un numero e imprimir su tabla de multiplicar. De 0 al 100.

num = 0

while True:
    try:
        num = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("Ingrese un numero valido.")

for i in range(0, 101):
    print(f"{num} x {i} = {num * i}")

    