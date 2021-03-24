class Zakupy:
    nazwa = ""
    ilosc = 0
    jednostka = ""
    cena = 0

    def __init__(self, nazwa, ilosc, jednostka, cena):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.jednostka = jednostka
        self.cena = cena

    def wyswietl_produkt(self):
        print(self.nazwa, self.ilosc, self.jednostka, self.cena)

    def ile_produktu(self):
        print(str(self.ilosc) + "" + self.jednostka)

    def ile_kosztuje(self):
        price = self.cena * self.ilosc
        return price