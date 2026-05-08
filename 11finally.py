try:

    bolunen = int(input("Bolunen: "))
    bolen = int(input("Bolen: "))

    netice = bolunen / bolen

    print("Netice:", netice)

except ZeroDivisionError:
    print("Bolme emeliyyatlarinda xeta bas verdi. Bolen sifir ola bilmez.")

except ValueError:
    print("Daxil edilen deyerler tam eded ollmalidir.")

except Exception:
    print("Gozlenilmeyen bir xeta bas verdi.")

finally:
    print("Emeliyyat tamamlandi.")