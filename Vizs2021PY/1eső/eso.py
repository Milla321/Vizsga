"""Írjon programot, amely Kérje be az aktuális hét és az előző hét csapadékmennyiségét. A program írja ki, hogy nőtt, csökkent vagy nem változott a csapadék mennyisége. A programot eso.py néven mentse. 
Mentés: eső
"""
##  Talián Lászlóné, 2021-01-17, SZOFT I/1/E

print('Nagy János, 2021-01-17, SZOFT I/1/E')
print('A 001 feladat megoldása')
print('.........................')
print('Agazati 001 mintafeladat megoldása')

print('Csapadék mennyiség milliméterben:')

aktualis = input('Aktuális heti csapadék: ')
elozo = input('Előző heti csapadék: ')
	
if aktualis > elozo:
	print('Tőbb csapadék')
elif elozo > aktualis: 
	print('Kevesebb csapadék')
else:
	print('Nem változott')
	
