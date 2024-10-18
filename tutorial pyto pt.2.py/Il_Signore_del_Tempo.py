def t(ore,minuti,secondi):
	secondi += minuti*60 + ore*60*60
	return secondi
o = 3
m = 15
s = 12
print(f"{o} ore, {m} minuti e {s} secondi equivalgono a {t(o,m,s)} secondi")
#super easy, primo tentativo