#dati tre numeri interi indicare il minimo, il massimo e il medio.
while True:    
    try:
        num1 = int(input("\ninserisci un numero intero: "))
        num2 = int(input("inserisci un numero intero: "))
        num3 = int(input("inserisci un numero intero: "))
        break
    except:
        print("\ndevi inserire numeri interi, riprova")
if num1 > num2 and num1 > num3:
    print("\nIl maggiore é " + str(num1))
    if num2 > num3:
        print("Il medio è " + str(num2))
        print("Il minore è " + str(num3))
    elif num2 < num3:
        print("Il medio è " + str(num3))
        print("Il minore è " + str(num2))
    else:
        print(str(num2) + "e" + str(num3) + "sono uguali")
    
elif num2 > num1 and num2 > num3:
    print("\nIl maggiore é " + str(num2))
    if num1 > num3:
        print("Il medio è " + str(num1))
        print("Il minore è " + str(num3))
    elif num1 < num3:
        print("Il medio è " + str(num3))
        print("Il minore è " + str(num1))
    else:
        print(str(num1) + "e" + str(num3) + "sono uguali")
    
elif num3 > num1 and num3 > num2:
    print("\nIl maggiore é " + str(num3))
    if num1 > num2:
        print("Il medio è " + str(num1))
        print("Il minore è " + str(num2))
    elif num1 < num2:
        print("Il medio è " + str(num2))
        print("Il minore è " + str(num1))
    else:
        print(str(num1) + "e" + str(num2) + "sono uguali")
else: 
    print("I tre numeri inseriti sono uguali tra loro!")

#ftyhfuy

while True:    
    try:
        num1 = int(input("\ninserisci un numero intero: "))
        num2 = int(input("inserisci un numero intero: "))
        break
    except:
        print("\ndevi inserire numeri interi, riprova")

def parity(x):
    if x % 2 == 0:
        return True
    elif x % 2 == 1:
        return False
    else:
        print("Error404")
   
if parity(num1) or parity(num2):
    print("\nLa somma è: " + str(num1 + num2))
if parity(num1) and parity(num2):
    print("\nIl prodotto è: " + str(num1 * num2))
if not parity(num1) and not parity(num2):
    print("\nIl quoziente è: " + str(num1 / num2))
 





















