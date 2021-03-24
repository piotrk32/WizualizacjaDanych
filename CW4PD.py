# zad 1

# list1 = []


# for x in range(1,31):
#     x*=2
#     list1.append(str(x))
# print(list1)
# plik = open("mnozenie.txt", "w")
# plik.writelines(list1)

# zad 2

# plik = open("mnozenie.txt", "r")
# read = plik.readlines()
# print(read)

# zad 3

# with open("dane.txt", "w") as dane2:
#     dane2.write("xdxdxdxdxd")
# with open("dane.txt", "r") as dane2:
#     for line in dane2:
#         print(line)
# dane2.close()

# zad 4
import classes
from classes import *

# produkt = Zakupy.Zakupy("Kasza", 2, "Kg", 3.50)
#
# produkt.wyswietl_produkt()
# produkt.ile_produktu()
# print(produkt.ile_kosztuje())

# zad 5

ciag = Ciagi.Ciagi()
ciag.pobierz_parametry(1, 4, 7)
ciag.policz_elementy()
ciag.pobierz_elementy(1, 4, 7)
ciag.policz_sume()
ciag.wyswietl_wyrazy()
