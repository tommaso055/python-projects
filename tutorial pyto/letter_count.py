def letter_count(string):
    frequency = {}
    for letter in string:
        if letter in frequency:
            frequency[letter] += 1   
        else:
            frequency[letter] = 1
    return frequency

print(letter_count("Tommaso è una mosca zezè fastidiosa"))