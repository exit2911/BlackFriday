

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os

print(os.listdir("/Users/VyHo/Downloads")) # print files in directory

df = pd.read_csv("/Users/VyHo/Downloads/BlackFriday.csv")

df1= pd.read_csv("/Users/VyHo/Downloads/Workbook1.csv")

df.head()

df.info()
5
columns = ['User_ID','Gender']

df_subset = pd.DataFrame(df, columns = columns)

type(df_subset)
df_unique_buyers = df_subset.drop_duplicates(['User_ID','Gender'])

unique_male = len(df_unique_buyers[df_unique_buyers.Gender == 'M'])

unique_female = len(df_unique_buyers[df_unique_buyers.Gender == 'F'])

print("total unique samples = ", df_unique_buyers )
print("total unique male buyers = ", unique_male)
print("total unique female buyers = ", unique_female)

labels = 'Male','Female'

sizes = [(unique_male/len(df_unique_buyers))*100, unique_female/len(df_unique_buyers)*100]


explode = (0.1,0)

colors = ['#1e90ff', '#FF69B4']
          
plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90)

plt.axis('equal')
plt.show()

columns = ['User_ID','Gender','Purchase']

df_subset = pd.DataFrame(df, columns = columns)

type(df_subset)

#groupby gender and user_id and sum up purchase amounts

df_purchase = df_subset.groupby(['User_ID','Gender']).sum().reset_index()
df_purchase.head()

uniq_male = df_purchase[df_purchase.Gender == 'M']
uniq_female = df_purchase[df_purchase.Gender == 'F']

uniq_male['Purchase'].max()
uniq_male['Purchase'].min()
uniq_male['Purchase'].mean()
uniq_male['Purchase'].median()

sns.distplot(uniq_male['Purchase'])


uniq_female['Purchase'].max()
uniq_female['Purchase'].min()
uniq_female['Purchase'].mean()
uniq_female['Purchase'].median()

sns.distplot(uniq_male['Purchase'])
      
sns.violinplot(x="Gender", y="Purchase", kind="violin", split=True,palette="pastel",data=df_purchase) #violin distribution plot


sns.countplot(x = 'Gender', data = df, palette = sns.color_palette('husl',2) )



sns.countplot(x='Marital_Status', data=df, palette= sns.color_palette("husl", 2))

sns.countplot(x='Gender', hue = 'City_Category', data = df, palette = sns.cubehelix_palette(3))

plt.figure(figsize = (20,10))

sns.countplot(x='Gender',hue='Product_Category_1', data = df, palette = sns.cubehelix_palette(18))
