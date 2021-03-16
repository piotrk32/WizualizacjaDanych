from random import *
# zad 1

#
#
# a = [ 1 -x for x in  range(1, 11, 1)]
# print(a)
#
# b = [ 4**y for y in range(8)]
# print(b)
#
# c = [x for x in b if x % 2 == 0]
# print(c)

# zad 2

# list1 = [randint(0, 100) for i in range(10)]
#
# print(list1)
#
# list2 = [i for i in list1 if i != 0 and i%2 == 0]
# print(list2)

# zad 3

# products = {"jaja": "sztuki", "mleko" : "kartony", "mieso" : "kg", "woda" : "litry"}
#
# list1 = [i for i in products.keys() if products[i] == "sztuki"]
# print(list1)

#  zad 4
#
# def ftrojkat(a,b,c):
#         if ((a+b>c) and (a+c>b) and (b+c>a)):
#             if ((a*a+b*b==c*c) or (a*a+c*c==b*b) or (c*c+b*b==a*a)):
#                 print("To jest trójkąt prostokątny")
#             else:
#                 print("To nie jest trójkąt prostokątny")
#         else:
#             print("Nie można zbudować trójkąta")
#
# a = int(input("Podaj pierwszy bok trojkata :"))
# b = int(input("Podaj drugi bok trojkata :"))
# c = int(input("Podaj trzeci bok trojkata :"))
# print(ftrojkat(a,b,c))

# zad 5


# def polet(a=2.5, b=4, h=10):
#     if (a > 0 and b > 0 and h > 0):
#         return ((a + b) * h) / 2
#     else:
#         print("Dlugosci podstaw ani wysokosc nie moze rownac sie 0")
#
# print("Pole trapezu wynosi : ", polet(), "[j^2]")

# zad 6

# def ilciag(a1=1, q=4, n=10):
#     an = a1*q
#     el = [a1,an]
#     iloczyn = a1*an
#     for x in range (3, n+1, 1):
#         wyr = an * q
#         el.insert(x, wyr)
#         an = wyr
#         iloczyn *= wyr
#
#     return iloczyn, el
# print(ilciag(1, 2, 10))

# zad 7

# def ileciag(* elementy):
#     if len(elementy) != 0:
#         iloczyn = 1
#         for x in range(len(elementy)):
#             iloczyn *= elementy[x]
#         return iloczyn
#     else:
#         return 0
# print(ileciag(1, 2, 3, 4, 5, 6))

# zad 8

# def sklep(** produkty):
#     iloscp = len(produkty)
#     print("Produktow jest :", iloscp)
#     if iloscp == 0:
#         print("brak zakupow")
#     else:
#         if iloscp != 0 :
#             sum = 0
#             for price in produkty.values():
#                 sum+=price
#         return sum
# print(sklep(jaja = 2, ser = 3, cytryna =1 ))