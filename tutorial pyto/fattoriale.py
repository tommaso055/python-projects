k = int(input())

#funzione fattoriale [1]
def fattoriale(n):
    result = 1
    k = n+1
    for i in range(1,k):
        result = result * i
    return result

print(fattoriale(k))



#funzione fattoriale [2]
def fattoriale(n):
    result = 1
    k = 0
    while k < n:
        k += 1
        result = result * k
    return result
#print(fattoriale())