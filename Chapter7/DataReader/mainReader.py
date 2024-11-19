import matplotlib.pyplot as plt
import pandas_datareader as pdr
df = pdr.get_data_fred('GS10')
plt.plot(df)
plt.show()


