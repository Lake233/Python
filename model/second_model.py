import pandas as pd
from matplotlib import pyplot as plt

file_path = 'e:\\document\\math model\\final model homework\\Chinese virus data.xlsx'
sheetname = 'Sheet1'
DF = pd.read_excel(file_path, sheet_name=sheetname)

increased = DF[['y']]
I = increased.drop([23,24])
plt.plot(I)
plt.show()