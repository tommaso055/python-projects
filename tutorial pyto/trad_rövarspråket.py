def trad_rövarspråket(string):
    translation = ""
    for letter in string:
        if letter in "aeiou ":
            translation += letter
        else:
            translation += letter + "o" + letter
    return translation
print(trad_rövarspråket("treno a vapore"))