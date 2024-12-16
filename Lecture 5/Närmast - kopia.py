# Skriv ett program som läser in en serie heltal och ett målvärde från användaren.
# Programmet skriva ut det tal i serien som ligger närmast det angivna målvärdet. Det
# sökta talet kan vara antingen större eller mindre än målvärdet. Om fler än ett heltal
# ligger lika nära målvärdet ska programmet skriva ut det första av dem. Programmet
# ska kunna hantera positiva såväl som negativa tal.

# Läs in tal från användaren
user_input = input('Ange en serie heltal, åtskilda av mellanslag: ')
# Omvandla strängen till en lista
user_list = user_input.split()
# Omvandla varje element i listan till ett heltal
numbers = [int(tal) for tal in user_list]
# Läs in ett målvärde från användaren och gör om till heltal
goal = int(input('Ange ett målvärde: '))

closest = numbers[0]
minstaSkillnaden = abs(goal - closest)

for i in numbers:
    skillnaden = abs(goal - i)
    if skillnaden < minstaSkillnaden:
        closest = i
        minstaSkillnaden = skillnaden
    elif skillnaden == minstaSkillnaden:
        continue

# Skriv ut resultatet: Definiera först closest
print('Närmast:', closest)
