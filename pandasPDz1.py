import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd




x = [2005, 2010, 2015, 2016, 2017 ]
y = [364.4, 413.3, 369.3, 382.3, 402.0]
plt.plot(x,y)
plt.title("Urodzenia żywe (w tys.) ")
plt.xlabel("rok")
plt.ylabel("tys. urodzeń")
plt.show()