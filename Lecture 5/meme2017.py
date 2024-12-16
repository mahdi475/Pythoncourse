# I ett meme från 2017 med SvampBob Fyrkant (Mocking SpongeBob) blandas små och stora
# bokstäver för att håna något eller någon. Skriv ett program som läser in ett ord från
# användaren och skriver ut ordet men med varannan bokstav liten och varannan bokstav
# stor. Den första bokstaven ska vara liten.

# Ex: meme    -> mEmE
#     SvampBob-> sVaMpBoB
#     FYRKANT -> fYrKaNt

word = input('Ange ett ord: ')

resultat = []

for i in range(len(word)):
    if i % 2 == 0:
        resultat.append(word[i].lower())
    else:
        resultat.append(word[i].upper())

print(''.join(resultat))
