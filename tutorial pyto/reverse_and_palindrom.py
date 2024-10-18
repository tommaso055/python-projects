string = input()

#Reverser
def reverse(string):
    result = ""
    for letter in string:
        result = letter + result
    return result

print(reverse(string))

#check if a num is palindrom
def pal(string):
    if string == reverse(string):
        return True
    else: 
        return False
        
print(pal(string))