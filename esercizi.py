#def create_phone_number(n):
#    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

#def create_phone_number(n):
#    n = ''.join(map(str,n))
#    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

#def create_phone_number(n):
#    str1 =  ''.join(str(x) for x in n[0:3])
#    str2 =  ''.join(str(x) for x in n[3:6])
#    str3 =  ''.join(str(x) for x in n[6:10])
#    return '({}) {}-{}'.format(str1, str2, str3)

#def create_phone_number(n):
#    m = ''.join(map(str, n))
#    return f"({m[:3]}) {m[3:6]}-{m[6:]}"

#def disemvowel(string):
#    return string.translate(None, 'aeiouAEIOU')



#def xo(s):
#    x_count = 0
#    o_count = 0
#    for letter in s:
#        if letter.lower() == "x":
#            x_count += 1
#        elif letter.lower() == "o":
#            o_count += 1
#    if x_count == o_count:
#        return True
#    else:
#        return False

#def xo(s):
#    l = list(s.lower())
#    if l.count("x") == l.count("o"):
#        return True
#    else:
#        return False

#Woooo, l'ho accorciato da solo!

def find_short(s):
    l = 8927987
    i = 0
    for letter in s:
        if letter != " ":
            i += 1
        elif i != 0 and i < l:
            l = i
            i = 0
    return l

print(find_short("bitcoin take over the world maybe who knows perhaps"))
