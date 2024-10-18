carciofo = [7,7,4,7,7,8,8,4]

def istogramma(list):
    for num in list:
        line = ""
        for unit in range(num):
            line += "*"
        print(line)

istogramma(carciofo)