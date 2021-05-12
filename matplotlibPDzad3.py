import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


t = np.arange(0, 30, 0.01)
s1 = np.sin(0.1*np.pi*t)
s2 = np.cos(0.1*np.pi*t)

plt.figure(1)
plt.subplot(211)
plt.plot(t, s1)
plt.title('Wykres wartości sinusa i cosinusa')

plt.xlabel('wartość y')
plt.ylabel('wartość x')
plt.plot(t, s2)
plt.xlabel('wartość y')
plt.ylabel('wartość x')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()