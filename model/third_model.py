import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math

file_path = 'e:\\document\\math model\\final model homework\\Chinese virus data.xlsx'
sheetname = 'Sheet1'
DF = pd.read_excel(file_path, sheet_name=sheetname)

y = DF[['y']].drop([23,24])
y = np.array(y).ravel()
x = np.array(range(1, len(y) + 1, 1))

def func(x, a, u, sig):
    return a*np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (sig * math.sqrt(2 * math.pi))

popt, pcov = curve_fit(func, x, y)

print('a = %.4f'%popt[0])
print('u = %.4f'%popt[1])
print('sig = %.4f'%popt[2])
plt.plot(x, y)
plt.plot(x, func(x, *popt))
plt.show()