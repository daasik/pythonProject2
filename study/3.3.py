import numpy as  np
import pandas as pd

# d = {'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C':[1,2,3]}
# df = pd.DataFrame(d)
# df.index.names = ['Nmb']
# a = df.dropna(thresh=2)
# s = df.fillna(value="FillMe")
# n = df['A'].fillna(value=df['A'].mean())
# print(n) and None


data = {'Company':['GooG', 'GooG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa','Carl', 'Sarah'],
        'Sales': [200,120,340,124,243,350]}
df = pd.DataFrame(data)
#print(df)
a = df.groupby('Company')
b = a.describe().transpose()['FB']
print(b)