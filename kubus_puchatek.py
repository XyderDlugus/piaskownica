import requests

link = 'http://xyder-dlgdaw.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

kubus_linie_b = kubus_text.split('</p>')

kubus_linie = []
for l in kubus_linie_b:
	l = l.replace('<p>', '')
	l = l.strip()
	kubus_linie.append(l)

koszyk = ['jablko', 'maliny', 'mango', 'agrest']

start = 1
end = 1000
tajemniczy_bohater = 'Darth Vader'
bohater_2 = 'Voldemort'
bohater_3 = 'Harry Potter'
for index, linia in enumerate(kubus_linie):
	if index >= start and index < end:
		
		linia = linia.replace('Kubuś',tajemniczy_bohater)
		linia = linia.replace('Puchatek', tajemniczy_bohater)
		linia = linia.replace('Królik', bohater_2)
		linia = linia.replace('Prosiaczek', bohater_3)
		linia = '<p>' + linia +' </p>'
		print(linia)
print()
print('<p>Czytała Krystyna Czubówna</p>')
	#if 'Kubus' in l:
	#	print(i,l)

#print( len( kubus_linie ) )
