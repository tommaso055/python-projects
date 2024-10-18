x = input("Di cosa vuoi calcolare l' area? ")
def area(fig):    
    if fig == "cerchio":
        r = float(input("Quanto misura il raggio? "))
        print(r*r*3.1415)
    elif fig == "quadrato":
        l = float(input("Quanto misura il lato? "))
        print(l*l)
    elif fig == "rettangolo":
        b_r = float(input("Quanto misura la base? "))
        h_r = float(input("Quanto misura l' altezza? ")) 
        print(b_r*h_r)
    elif fig == "triangolo":
        b_t = float(input("Quanto misura la base? "))
        h_t = float(input("Quanto misura l' altezza? "))
        print((b_t*h_t)/2)
    else:
        print("Non sono in grado di calcolare l'area di questa figura. Prova con un'altra: ")
                
area(x)   