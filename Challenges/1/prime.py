# 2) Imprimir los numeros primos entre 0 y 10000.

for i in range(0,1000):
    if i == 1 or i == 0:
        continue
    if i == 2:
        print(i)
        continue 
    for j in range(2, i//2):
        if i % j == 0:
            break
    else:
        print(i)
    
    