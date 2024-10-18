while True:  
    num1 = float(input("\nWrite a number: "))
    operator = input("write an operator:")
    num2 = float(input("Write another number: "))
    if operator == "+":
        result = num1 + num2
        
    elif operator == "-":
        result = num1 - num2
    
    elif operator == "*":
        result = num1 * num2
    
    elif operator == "/":
        result = num1 / num2
    
    else:
        result = "invalid operator"
    print(result)