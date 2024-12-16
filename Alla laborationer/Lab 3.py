ord = input("Skriv in ett ord: ")

nytt_ord = ord
separeradeOrd = ord.split()

vokaler = 'aeiouyåäö'

sista_vokalen_index = -1 #vi antar att ingen vokal finns

resultat = []

#hitta den sista vokalen
for i in range(len(ord)):
    if ord[i].lower() in vokaler:
        sista_vokalen_index = i

if sista_vokalen_index != -1:
    sista_vokalen = ord[sista_vokalen_index] * 3
    nytt_ord = ord[:sista_vokalen_index] + sista_vokalen + ord[sista_vokalen_index +1:] #skriver om gamla 


print(nytt_ord)