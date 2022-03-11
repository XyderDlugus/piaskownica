import requests 
link = 'http://zajecia-programowania-xd.pl/flagi'
flagi_response = requests.get(link)
flagi_tekst = flagi_response.text
print (flagi_tekst)

lista = [1, 2, 3]
flagi = flagi_tekst.split('</p>')
for f in flagi:
	if 'http://' in f:
		f = f[3:]
	print('-',f)
#flagi = ['link1', 'link2', 'link3']
#flagi_text



#Listy 
#lista = [1, 2, 3]

#lista = ['1','2','3']
#lista = 'abcdefg'
#dlugosc_listy = len(lista)
#print ('Dlugosc:',dlugosc_listy)

#element = lista[5]
#print('Element:', element)

#for i in lista:
#	print(i)
