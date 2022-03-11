dzien = 'Sr'

#if dzien == dzisiaj:
#	print('Tak dzisiaj sroda')
#print(dni_robocze)
#print(weekend)
if dzien in dni_robocze:
	print('Dzisiaj jest dzien pracujacy')
elif dzien in weekend:
	print('Dzisiaj jest weekend')
else:
	print('Zle napisales dzien tygodnia')	

dni_robocze = [
	'Pon',
	'Wt',
	'Sr',
	'Czw',
	'Pt',
]
weekend = [
	'Sob'
	'Nd'
]
