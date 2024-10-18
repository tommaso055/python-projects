trenino = ["carciofo","treno","due","tremore","overthinking"]

def x(list):
    lunghezza_parole = []
    for word in list:
        letters = 0
        for letter in word:
            letters += 1
        lunghezza_parole.append(letters)
    return lunghezza_parole

print(x(trenino))
