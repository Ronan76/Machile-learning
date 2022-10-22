# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 09:31:32 2022

@author: 202257
"""

import pandas as pd
a = pd.read_csv("C:/Users/202257/Machile-learning/batchs/restaurant_1_week_002.csv")
import os, glob
import pandas as pd

path = "C:/Users/202257/Machile-learning/batchs"
def extract(data_dir:str, start_week:int, end_week:int, prefix:str) -> pd.DataFrame:
    df = pd.DataFrame()
    for i in range(start_week,end_week+1):
        file_path = os.path.join(data_dir, "batchs",f'{prefix}_week_{i}.csv')
        batch = pd.read_csv(file_path)
        df = pd.concat([df,batch], sort=True)
    return df

df1 = extract("C:/Users/202257/Machile-learning/", 197, 200, 'restaurant_1')

df1 = df1.assign(CA = df1['Product Price'] * df1['Quantity'])

df1_gb =  df1.groupby(by='Order Date').mean('CA')

print(df1)

def clean(df1: pd.DataFrame) -> pd.DataFrame:
    df1.columns = df1.columns.str.lower().str.replace(' ','_')
    df1.head()
    
    
    df1.order_date = pd.to_datetime(df1.order_date)
    df1.dtypes
    
     
    df1['total_product_price'] = df1['product_price'] * df1['quantity']
    df1['cash_in'] = df1.groupby('order_number')['total_product_price'].transform(np.sum)
    df1 = df1[['order_date', 'order_number', 'cash_in']]
    df1 = df1.drop_duplicates()
    df1 = df1.reset_index(drop=True)
    return df1

df1 = clean(df1)

def resample(df1: pd.DataFrame) -> pd.DataFrame():
    df1 = df1.resample('1H', on ='order_date').sum().reset_index()
    return df1
df1 = resample(df1)


import matplotlib.pyplot as plt
fig= plt.figure(figsize=(10,5))
plt.plot(df1.order_date, df1.cash_in)
plt.xlabel('time')
plt.ylabel('turnover')
plt.grid(True)





df1.resample('1H', on='order_date').sum().reset_index()

    
df1_gb =  df1.groupby(by='order_date').mean('CA')
#######graphique


import numpy as np


xpoints = np.array(df1_gb['order_date'])
ypoints = np.array(df1_gb['CA'])


plt.plot(df1_gb['order_date'], df1_gb['CA'])
plt.show()




























rst1 = glob.glob(os.path.join(path, "restaurant_1*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)
    
merged_rst1 = pd.concat(all_df, ignore_index=True, sort=True)


print(merged_rst1)


rst2 = glob.glob(os.path.join(path, "restaurant_2*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)
    
merged_rst1 = pd.concat(all_df, ignore_index=True, sort=True)


print(merged_rst2)



a = pd.read_csv("C:/Users/202257/Machile-learning/batchs/restaurant_1_week_002.csv")



a.Quantity * a.
merged_df_groupby = merged_df.groupby(by='file').mean('Product Price'*'Quantity')


