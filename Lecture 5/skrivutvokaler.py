def skriv_ut_vokaler():
    vokaler = 'aouåeiyäöAOUÅEIY'

    text = input()
    #resultat = [i for i in text if i in vokaler]

    resultat=[]
    for bokstav in text:
        if bokstav in vokaler:
            resultat.append(bokstav)

    print("".join(resultat))

skriv_ut_vokaler()
