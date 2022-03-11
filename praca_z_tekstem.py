import requests
def policz_znaki(argument):
	liczba_znakow = len(argument)
	return policz_znaki

link = 'http://xyder-dlgdaw.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

#Zabawa z indeksem
#link_b link[10]
#link_b = link[::-1]
#link_b = link[1:-1]

#Metody wbudowane
#link_b = link.upper()
#link_b = link.lower()

# Dodawanie ciagow znakow
#link_b = link[:20] + ' ' + link[20:]

#link_b = link[:20].upper() + '                                       ' + link[20:]


ciag = "abcd  abcd  abcd "
efekt = ciag.split("d")
print() 
print(ciag)
print(efekt)
print()
