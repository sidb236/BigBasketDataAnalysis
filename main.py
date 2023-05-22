

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#%%

all_df = pd.read_csv('BigBasket Products.csv')
sample_products = all_df.sample(10)


#%%
sum_null = all_df.isnull().sum()

#%%
fig, ax = plt.subplots(figsize=(15, 10))
sns.barplot(y= 'market_price', x='category', data= sample_products)
plt.show()

#%%
all_df['Discount'] = all_df['market_price']-all_df['sale_price']
print(all_df)
all_df.drop(columns='Profit')
#%%
fig, ax = plt.subplots(figsize = (15, 10))
sns.distplot() #change here
plt.show()

