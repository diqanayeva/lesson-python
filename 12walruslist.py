yemekler = list()

while True:
    yemek = input( 'Hansi yemeyi sevirsiniz?')
#while yemek := input("Hansi yemeyi sevirsiniz?") != 'cix'

    if yemek == 'cix':
        break

    yemekler.appened(yemek)

print(yemekler)
