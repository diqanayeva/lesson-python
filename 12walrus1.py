def boyuk( metn):
    return metn.upper(git )



def kicik(metn):
    return metn.lower()


#print(boyuk('hello'))
#print(kicik('HELLO'))

def ekranaYazdir(f):
    netice = f('heLLo')
    print(netice)

ekranaYazdir(boyuk)
ekranaYazdir(kicik)    