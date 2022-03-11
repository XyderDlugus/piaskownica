import requests
url = "https://zajecia-programowania-xd.pl/flagi"
surowe_info = requests.get(url)
text = surowe_info.text
#Przygotowanie listy linków ze strony
efekt = text.split('</p>')
linki = []
for linia in efekt:
    link = linia.replace('<p>', '' )
    link = link.replace('- ', '' )
    link = link.strip()

    if ' 'in link or '<' in link:
        continue
    linki.append( link)

#CEL:
#Policz ile jest domen z .pl

#Realizacja
domeny_pl = 0
domeny_com = 0
domeny_x = 0
wszystkie_kropki = 0
n_domen_pl = 0
for i, link in enumerate(linki):
    if '.pl' in link:
        domeny_pl += 1
    if '.com' in link:
        domeny_com += 1
    if ('.pl' in link) and ('.com' in link):
        domeny_x +=1

for link in linki:
        if link.count('.') > 1:
                continue
        elif '.pl' in link: 
            n_domen_pl += 1
print('Liczba domen pl wynosi:', n_domen_pl)
#print(domeny_pl)
#print(domeny_com)
#print(domeny_x)