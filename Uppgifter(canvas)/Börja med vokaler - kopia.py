# Skriv ett program som läser in en serie ord från användaren. Programmet skriva ut de ord
# i serien som börjar på vokal. Vokaler är bokstäverna aouåeiyäö. Orden ska skrivas ut på
# samma rad, åtskilda av mellanslag. Programmet ska kunna hantera små och stora bokstäver.
# Orden ska skrivas ut så som de skrivits av användaren.

# Läs in ord från användaren
user_input = input('Ange en serie ord, åtskilda av mellanslag: ')
# Omvandla strängen till en lista av strängar
words = user_input.split()

vokaler = 'aeiouyåäö'

resultat = []

for word in words:
    if word[0].lower() in vokaler:
        resultat.append(word)

print(' '.join(resultat))