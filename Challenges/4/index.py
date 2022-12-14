# - Imprimir por pantalla los elementos del CSV del archivo de example.csv
# Utilizar el método readlines.
with open("./example.csv", "r") as file:
    content = file.readlines()


header = content[0]

body = content [1:]

# lista de elementos de header
header = header.split(",")
# quitar espacios en blanco y comillas
header = [x.strip().replace('"','') for x in header]
# lista de elementos de body
body = [x.split(",") for x in body]
# quitar espacios en blanco y comillas
body = [[y.strip().replace('"','') for y in x] for x in body]


for i in range(len(body)):
    row = body[i]
    max_length = max([len(x) for x in row])
    for j in range(len(row)):
        row[j] = row[j].ljust(max_length)
    body[i] = row

    for k in range(len(header)):
        header[k] = header[k].ljust(max_length)

print(" | ".join(header))
for row in body:
    print(" | ".join(row))

