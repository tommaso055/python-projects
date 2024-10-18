def Poesia_Elettronica(word, lista):
	rhyming_words = []
	for item in lista:
		if list(word)[-3:] == list(item)[-3:]:
			rhyming_words.append(item)
	return rhyming_words

parole = ["carote", "carciofi", "cacata"]
print(Poesia_Elettronica("patata", parole))