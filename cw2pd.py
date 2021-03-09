
# zad 1


# lista = ['koszykowka', 'siatkowka', 'football', 'mma']
# print(lista)
# lista.append('curling')
# lista.append('surfing')
# print(lista)
# lista.reverse()
# print(lista)

# zad 2

# slownik = {"np" : "na przyklad", "itd" : "i tak dalej", "ps" : "post scriptum"}
# print(dict.values(slownik))
# print(slownik)

# zad3

# gamedict = {"1" : "CS GO", "2" : "Rainbow Six Siege", "3" : "Call Of Duty", "4" : "LOL", "5" : "DOTA 2", "6" : "HoTS"}
# print(dict.items(gamedict))

# zad4

# string = input("Podaj wyrazenie :")
# count = 0
# for i in string:
#     if i == "a":
#         count += 1
# print(count)

# zad 5
# a = input("Podaj pierwsza liczbe calkowita :")
# b = input("Podaj pierwsza druga calkowita :")
# c = input("Podaj pierwsza trzecia calkowita :")
#
# a = int(a)
# b = int(b)
# c = int(c)
#
# wynik = a**b + c
# print(wynik)

# zad 6
# a = input("Podaj pierwsza liczbe calkowita :")
# b = input("Podaj pierwsza liczbe calkowita :")
# c = input("Podaj pierwsza liczbe calkowita :")
#
# a = int(a)
# b = int(b)
# c = int(c)
#
# if a > b:
#     print(a, " jest najwieksze")
#     if b > a:
#         print(b, " jest najwieksze")
# else:
#     print(c, " jest najwieksze")

# zad 7

# list = [4, 4.11, 5, 5.23, 6, 6.89]
# for i in list:
#     print(i**2)

# zad 8
# trashlist =[]
# list = []
#
# while(len(trashlist) != 10):
#     a = input("Podaj liczbe ")
#     trashlist.append(a)
#     if int(a)%2 == 0:
#         list.append(a)
# print(list)

# zad 9

# list = [1,2,3,4,5]
#
# for i in list :
#     if i%2 !=0:
#         print("EEEEE")
#     if i%2 == 0:
#         print("E")

# zad 10
# import math
#
# a = int(input("Podaj liczbe do spierwiastkowania : "))
# if a == 0:
#     print("Brak pierwiastka")
# if a > 0:
#     print(math.sqrt(a))
# if a < 0:
#
#     try:
#         math.sqrt(a)
#     except ValueError:
#         print("Liczby ujemne mozna pierwiastkowac tylko na plaszczyznie zespolonej")

