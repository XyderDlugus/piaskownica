from lista_flag import stworz_liste_flag


def policz_domeny_pl(linki):
    wynik = 0
    #tu zaczyna się Twój kod.
    for flaga in lista_flag:
        if '.pl' in flaga:
            wynik += 1

    #Tu kończy się twój kod
    return wynik
url = "https://zajecia-programowania-xd.pl/flagi"
lista_flag = stworz_liste_flag(url)
    #Wyhaszuj na końcu te 2 linie
wynik = policz_domeny_pl(lista_flag)
print(wynik)