import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import date, datetime, time , timezone
path = '/Users/nyfong/coding/Python/Samsung_/project/estimated-cumulative-excess-deaths-per-100000-people-during-covid-19.csv'
df = pd.read_csv(path)

df['Date'] = pd.to_datetime(df['Day'])
df.set_index('Date', inplace= True)
df.drop(['Day'], axis=1, inplace= True)
df.head(20)
# df.info()