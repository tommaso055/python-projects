cavallo = [2,3,6,7]

#Sommatrice Inarrestabile
def somma(list):
    result = 0
    for num in list:
        result += num 
    return result

#Moltiplicatore Inarrestabile
def prodotto(list):
    result = 1
    for num in list:
        result *= num 
    return result

print(somma(cavallo))
print(prodotto(cavallo))