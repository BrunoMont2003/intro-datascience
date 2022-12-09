# 2)Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia' , 'Lengua']

asignaturas_notas = []

for asignatura in asignaturas:
    nota = ''
    while True:
        nota = input(f'Ingrese la nota de la asignatura {asignatura}: ')
        if nota:
            break
    nota = int(nota)
    asignatura_nota = (asignatura, nota)
    asignaturas_notas.append(asignatura_nota)

asignaturas_repetir = []
asignaturas_aprobadas = []
for asignatura,nota in asignaturas_notas:
    if nota < 11:
        asignaturas_repetir.append(asignatura)
    else:
        asignaturas_aprobadas.append(asignatura)

print('Asginaturas a repetir: ', ", ".join(asignaturas_repetir))
print('Asginaturas aprobadas: ', ", ".join(asignaturas_aprobadas))