def unit_conversion(meters):
    miglia = meters * 0.000621371
    yards = meters * 1.09361
    piedi = meters * 3.28084
    pollici = meters * 39.3701
    print(str(meters) + " metri sono uguali a " + str(miglia) + " miglia")
    print(str(meters) + " metri sono uguali a " + str(yards) + " yards")
    print(str(meters) + " metri sono uguali a " + str(piedi) + " piedi")
    print(str(meters) + " metri sono uguali a " + str(pollici) + " pollici")

metri = float(input("\ninserisci i metri: "))
unit_conversion(metri)
    