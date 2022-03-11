import requests


url = 'https://zajecia-programowania-xd.pl/flagi'
surowe_info = requests.get( url)
text = surowe_info.text

lista_linii = text.split('</p>')
linki = []

for linia in lista_linii:
    if linia:
        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.strip()
        if ' ' in link or '<' in link:
            continue
        linki.append( link)

def longest_string(lista) :
    najdluzszy = max(lista, key=len)
    najkrotszy = min(lista, key=len)
    return najdluzszy, najkrotszy

lista_z_flagami = longest_string(linki)

for l in lista_z_flagami:
    print(l, len(l))