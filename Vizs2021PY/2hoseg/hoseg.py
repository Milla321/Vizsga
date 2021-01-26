"""A program kérje be mért adatokat, majd írassa ki, hogy volt fagy. Fagyról 0 fok alatt beszélünk. Az adatok bekérése addig történjen, amíg 'vege' végjellel jelzi a felhasználó, hogy nem ad meg több adatot. A bemenő adatok lehetnek negatív és pozitív számok vagy nulla. A végjel esetén ne vizsgálja, hogy volt-e fagy. 
Mentés: hoseg 
"""
##  Talián Lászlóné, 2021-01-17, SZOFT I/1/E

print('Talián Lászlóné, 2021-01-17, SZOFT I/1/E')
print('A 002 feladat megoldása')
print('.........................')
print('Agazati 002 mintafeladat megoldása')

print('Hőmérsékletek:')

def fagy(ho):
	if (ho) < 0:
		return True
	else:
		return False
		
ho = ' '
while ho != 'vége':
	ho = input('Hő: ')
	if ho != 'vége':
		if fagy(int(ho)):
			print('Fagy volt')
		else:
				print('Nem volt fagy')				
