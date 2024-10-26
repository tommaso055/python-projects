import math
for lati in range(3,11):
  misura_lato = float(lati)
  nfisso = math.tan((misura_lato-2)/(2*misura_lato)*3.14159)/2
  lunghezza_lato=1
  perimetro = float(lati)*lunghezza_lato
  apotema = lunghezza_lato* nfisso
  area = (perimetro * apotema) / 2  
  area = area / (math.sqrt((apotema)**2 + 0.25)*2)
  print (lati,nfisso, area)