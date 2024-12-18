# Läs in ett serie av dagar från användaren
user_data = input('Skriv in dagar (0-6): ')

user_data_split = user_data.split()

dagar = [int(num) for num in user_data_split]

veckordagar = ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag', 'lördag', 'söndag']

for dag in dagar:
    print(veckordagar[dag])

    


