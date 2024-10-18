#def. variabili
miglior_drink = "martini"
prezzo_drink = 5.5

#programma
print("Buonasera e benvenuto al miglior pub della città!")
print("Io sono Tommaso e ti servirò al bancone")
print("Come ti chiami?")
nome_cliente = input()
print("Ottimo, " + nome_cliente + ", in che anno sei nato?")
anno_nascita = int(input())
età_cliente = 2022-anno_nascita
menù = ["coca cola","sprite","succo di frutta","gin tonic","vodka tonic","mojto","caipirinha","caipiroska","negroni"]
print("\n Ecco il menù:")
for drink in menù:
    if drink == "gin tonic" and età_cliente < 18:
        break
    print(drink + str(prezzo_drink)+"$")
print("\nCosa vuoi ordinare?")    
drink_ordinato = input()
print("hai una carta fedeltà?")
risposta = input()
if risposta == "si":
    prezzo_drink -= 1.75
    print("ottimo, puoi andare a pagare in cassa")
elif risposta == "no":
    print("ok, puoi andare a pagare in cassa")
else:
    print("si o no?")
    risposta_2 = input()
    if risposta_2 == "si":
        prezzo_drink -= 1.75
        print("ottimo, puoi andare a pagare in cassa")
    else:
        print("ok, puoi andare a pagare in cassa")

print("\nIl totale é " + str(prezzo_drink) + "$, come vuole pagare?")
pagamento = input()
print("D'accordo, ecco a lei e arrivederci")
