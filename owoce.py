# Lista
lista = [1, 2 ,3, 4]
koszyk =['jabłko1', 'jabłko2', 'jabłko3','garsc malin'] #napisy typ:str string
#Pętla


print('Zaczynam')

for owoc in koszyk:
	print('1. Wyciagam', owoc)
	print('2. Myje', owoc)
	print('3. Zjadam', owoc)

	if owoc == 'garsc malin':
		continue

	print('4. Wyrzucam ogryzek po', owoc)
	print()
print ('Skonczylem')
