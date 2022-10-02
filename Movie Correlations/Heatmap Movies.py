#import libraries
import numpy as np
import os
import re
import pandas as pd
import seaborn as sb
import csv
import matplotlib
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
plt.style.use("ggplot")
from matplotlib.pyplot import figure

matplotlib.rcParams['figure.figsize']=(12,8)

#READ IN THE DATA
full_path = os.path.realpath(__file__)
file_path = os.path.dirname(full_path)

result=pd.read_csv(file_path+'\\movies2.csv')
df=pd.DataFrame(result)
df=df.sort_values(by='gross',ascending=False)
with pd.option_context("display.max_columns", None):
    print(df.head())
print("\n")
print("SHOW THE PERCENTAGE OF MISSING DATA")
print("\n")
print("Category - Percent Missing Data")
for col in df.columns:
    percentmissing=np.mean(df[col].isnull())
    print("{} - {}".format(df[col].name,percentmissing))

#print(df.dtypes)
#Finding ratings

print(df['rating'].unique())
print(df['rating'], df['rating'].value_counts())


#THIS WAS ALL FOR SCRUBBING THE DATA, IT'S UNNEEDED NOW THAT
#THIS CODE ANALYSES CLEANED DATA
'''
df["released"]=df['released'].astype(str)
df["year_correct"]=df['released'].astype(str)
df["location_correct"]=df['released'].astype(str)
#print(df["year_correct"][4])
count=0
store = [0, 0, 0, 0]
for x in range(len(df)):
    for m in df["released"][x][::-1]:
        if m.isdigit():
            name=df["released"][x].split(m)[-1]
            name=name.replace("(","")
            name=name.replace(")","")
            name=name.lstrip()
            #print(name)
            df["location_correct"][x]=name
            break
#print(df["location_correct"])
#print(df['year_correct'])

for x in range(len(df)):
    for m in df["year_correct"][x]:
        if m.isdigit():
            store[count] = m
            count += 1
            if count == 4:
                df['year_correct'][x]= "%s%s%s%s" %(store[0],store[1],store[2],store[3])
                count = 0
                store = [0, 0, 0, 0]
                pass
        # print("%s%s%s%s" %(store[0],store[1],store[2],store[3]))
        else:
            count = 0
            store = [0, 0, 0, 0]

#print(df["year_correct"])
df.to_csv('C:\\Users\\magla\\Desktop\\Data and Coding\\movies2.csv')

'''
#Plot the scatterplot b/w budget and gross income
plt.scatter(x=df['budget'],y=df['gross'])
plt.title("Budget vs Gross Income")
plt.xlabel("Budget")
plt.ylabel("Gross Income")
plt.show()

#Plot budget vs gross w seaborn
sb.regplot(x=df["budget"],y=df["gross"],scatter_kws={"color":"red"},line_kws={"color":"blue"})
plt.title("Budget vs Gross Income")
plt.xlabel("Budget")
plt.ylabel("Gross Income")
plt.show()

#Start looking for correlation
print("---------CORRELATIONS-------------")
print("With Pearson")
with pd.option_context("display.max_columns", None):
    print(df.corr()) #pearson(default), kendall, spearman
    print("\n")
    print("With Spearman")
    print(df.corr(method='spearman'))
    #print("With Kendall")
    #print(df.corr(method='kendall')) Kendall fails

sb.heatmap(df.corr(),annot=True)
plt.title("Correlation Matrix of Movie Factors")
plt.xlabel("Movie Factors")
plt.ylabel("Movie Factors")
plt.show()

#Numerize data for an enhanced heatmap

df_numerized=df
# Organize ratings

df_numerized['rating']=df_numerized['rating'].replace("G",1)
df_numerized['rating']=df_numerized['rating'].replace("PG",2)
df_numerized['rating']=df_numerized['rating'].replace("PG-13",3)
df_numerized['rating']=df_numerized['rating'].replace("TV-14",3)
df_numerized['rating']=df_numerized['rating'].replace("TV-MA",4)
df_numerized['rating']=df_numerized['rating'].replace("NC-17",4)
df_numerized['rating']=df_numerized['rating'].replace("R",5)
df_numerized['rating']=df_numerized['rating'].replace("X",6)
df_numerized['rating']=df_numerized['rating'].replace("Unrated",float('nan'))
df_numerized['rating']=df_numerized['rating'].replace("Approved",float("nan"))
df_numerized['rating']=df_numerized['rating'].replace("Not Rated",float('nan'))
df_numerized['rating']=df_numerized['rating'].replace("nan",float("nan"))

#for value in df_numerized['rating']:
   #print(value)

for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype=='object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes

#with pd.option_context("display.max_columns", None):
    #print(df.head())
#print(df_numerized['rating'].unique())

sb.heatmap(df.corr(),annot=True)
plt.title("Correlation Matrix of Movie Factors")
plt.xlabel("Movie Factors")
plt.ylabel("Movie Factors")
plt.show()

