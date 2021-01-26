"""A következő feladatban eladó kocsik adatait tároljuk egy fájlban. A fájl beolvasása után, ki kell íratnia azoknak a kocsiknak az adatait, amelyek ára kevesebb mint 1 millió. Utána ki kell íratnia egy újabb sorban, azokat amik 1 millió forint alatti áron vannak és fehérek. 
Mentés: eladas.py 
"""

##  Talián Lászlóné, 2021-01-17, SZOFT I/1/E
from jarmu import Jarmu

print('Talián Lászlóné, 2021-01-17, SZOFT I/1/E')
print('A 003 feladat megoldása')
print('.........................')
print('Agazati 003 mintafeladat megoldása')

print('Járművek eladása:')

class Eladas:
	def olvas_file(self):
		print("Beolvasas  ")
        self.jarmuvek = []
        fp = open('jarmu.txt', 'r')
        lines = fp.readlines()        
        for line in lines[1:]: 
			 line = line.rstrip()
            (az, rendszam, szin, marka, ar) = line.split(':')
            jarmu = Jarmu(az, rendszam, szin, marka, int(ar))
            self.jarmuvek.append(jarmu)
         fp.close()   
        	        
	def feher(self):
		count = 0
		for jarmu in self.jarmuvek:
			if jarmu.szin == 'fehér':
				count += 1 
         print('Fehér járművek:', count)
	
	def olcso(self):
        print('Olcsó járművek:')
        for jarmu in self.jarmuvek:
            if int(jarmu.ar) < 1000000:
                print(jarmu.rendszam, jarmu.szin, jarmu.marka);
                
      def feherOlcso(self):
        print('Olcsó fehér járművek fájlba:')
         fp = open('feherOlcso.txt', 'w')
         for jarmu in self.jarmuvek:
             if int(jarmu.ar) < 1000000 and jarmu.szin == 'fehér':
        
        for jarmu in self.jarmuvek:
            if int(jarmu.ar) < 1000000 and jarmu.szin == 'fehér':
				
                fp.write(
                jarmu.az + 
                ":" + jarmu.rendszam + 
                ":" + jarmu.szin + 
                ":" + jarmu.marka + 
                ":" + jarmu.ar + "\n"                
                )
        fp.close()
 
  
eladas = Eladas()
eladas.olvas_file()
eladas.feher()
eladas.olcso()

eladas.feherOlcso()
