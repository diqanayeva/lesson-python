try:

    bolunen = int(input("Bolunen: "))
    bolen = int(input("Bolen: "))

    netice = bolunen / bolen

    print("Netice:", netice)

except Exception as e:
    print("Xeta:", e)