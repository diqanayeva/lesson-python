telebeler = [
    ( "Ali", "F", 45),
    ("Veli", "A", 85),
    ("Ayse", "D", 60),
    ("Mehemmed", "B", 75),
]

telebeler.sort()
#tuple 2 ve 3 derecesine gore tapmaq
#telebeler.sort(key = lambda dereceler:  )

derece = lambda dereceler: dereceler[1]

telebeler.sort(key = derece)

for i in telebeler:
    print(i)