import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd




df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)
grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']})
wykres = grupa.plot.bar(fontsize= 10, rot=0)

plt.legend(loc= 'lower right')
plt.title("Suma zamowien")
plt.xlabel("Sprzedawca")
plt.ylabel("Ilosc")
plt.show()

