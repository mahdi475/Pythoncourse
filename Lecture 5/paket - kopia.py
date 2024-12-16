maxvikt = int(input("Ange maxvikt (kg): "))

paketensVikt = 0
antalLastatPaket = 0

while paketensVikt < maxvikt:
    nuvarandePaket = int(input("Paketets vikt (kg): "))
    if (paketensVikt + nuvarandePaket) <= maxvikt:
        paketensVikt = paketensVikt + nuvarandePaket
        antalLastatPaket = antalLastatPaket + 1
    else:
        break

print(f'Du kan lasta {antalLastatPaket} paket. Totalvikten är {paketensVikt} kg.')