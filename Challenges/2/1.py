# 1) Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

moneda = ''
while True:
    moneda = input('Qué moneda desea obtener? ')
    if moneda:
        break

moneda = moneda.lower().capitalize()
simbolo = divisas.get(moneda, 'No se encontró la moneda')
print(simbolo)