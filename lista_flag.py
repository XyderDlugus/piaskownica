import requests
import sys, os
url = "https://zajecia-programowania-xd.pl/flagi"
def pobierz_tekst_ze_strony_www(url):
    
    surowe_info = requests.get(url)
    text = surowe_info.text
    return text

def stworz_liste_flag(url):
    text_strony_www = pobierz_tekst_ze_strony_www(url)
    efekt = text_strony_www.split('</p>')
    linki = []
    for linia in efekt:
        link = linia.replace('<p>', '' )
        link = link.replace('- ', '' )
        link = link.strip()

        if ' 'in link or '<' in link:
            continue
        linki.append( link)

    return linki

if __name__ == '__main__':
    argument = sys.argv[1]
    lista_flag = stworz_liste_flag(argument)
    print(lista_flag)
#url = "https://zajecia-programowania-xd.pl/flagi"