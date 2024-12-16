# Läs in ett par ord från användaren

user_data = input('Skriv in dina ord: ')
# Gör om till en lista

ord_lista = user_data.split()

versaler = []

for ord in ord_lista:
    if ord.isupper():
        versaler.append(ord)

for ord in versaler:
    print(ord)