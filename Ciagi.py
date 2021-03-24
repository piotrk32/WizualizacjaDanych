class Ciagi:
    a1 = 0
    roznica = 0
    ilewyrazow = 0
    wyrazy = [a1]

    def wyswietl_wyrazy(self):
        print(self.wyrazy)
    def pobierz_elementy(self, *n):
        pobrane = []
        for x in n:
            pobrane.append(self.wyrazy[x - 1])
            print(pobrane)
    def pobierz_parametry(self, a1, roznica, ilewyrazow):
        self.a1 = a1
        self.roznica = roznica
        self.ilewyrazow = ilewyrazow

    def policz_sume(self):
        suma = 0
        for x in self.wyrazy:
            suma += x
        print(suma)

    def policz_elementy(self):
        if self.roznica != 0:
            a1 = self.a1
            for x in range(self.ilewyrazow):
                an = a1 + self.roznica
                self.wyrazy.append(an)
                a1 = an


