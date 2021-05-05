import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd




chlopcy = [234, 231, 199, 201, 206, 205, 231]
dziewczynki = [211, 221, 233, 212, 205, 205, 221]
index = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
df = pd.DataFrame({'chlopcy': chlopcy,
                   'dziewczynki': dziewczynki}, index=index)
ax = df.plot.bar(rot=0)
plt.title("ilosc chlopcow i dziewczynek (w tys)")
plt.legend(loc='lower right')
plt.show()