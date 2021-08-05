# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:32:31 2021

@author: divas
"""

#import data into python
url= 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'

import pandas as pd
import numpy as np
df= pd.read_csv(url)
df
df.shape #dim of data
df.columns #name of columns
df.head(3)
df.tail(5)

# expand business by encouraging loyal customers to improve repeated sales. Loyal customers- How many times a particular customer bought these items.

# maximize revenue from high value parts 
# Screenshot
df.describe()

pd.options.display.float_format="{:.2f}".format

df.describe()
df['region']=df['region'].astype("category")
df.describe()
df.region.value_counts()
df.region.value_counts().plot(kind="bar")

#who are the most loyal customers?

df
df.custname.value_counts()
df.custname.value_counts().sort_values(ascending=False).head(5)

df.custname.value_counts().sort_values(ascending=True).head(5)




#Customer contributed to most of their revenue

y=df.groupby('custname').revenue.agg([np.sum,max])
y
type(y)
d=y.sort_values(by='sum').tail()
d.iloc[::-1]


#Another way

df.groupby('custname').revenue.sum().sort_values(ascending=False).head(5)
df.groupby('custname').aggregate({'revenue':[np.sum,max]}).sort_values(ascending=False).head(5)




















