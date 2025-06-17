import pandas as pd

df1 = pd.read_excel("DataSets\online_retail_II.xlsx",sheet_name='Year 2009-2010',engine='openpyxl')
df2 = pd.read_excel("DataSets\online_retail_II.xlsx",sheet_name='Year 2010-2011',engine='openpyxl')


df =pd.concat([df1,df2],ignore_index=True) #ignore_index it will start with again 0 onwards

print(df.shape)
print(df.columns)

print(df.info())
print(df.describe())

##Cleaning & Feature Engineering
df.dropna(subset=['InvoiceDate','Customer ID'],inplace= True)

print(df.shape)
print(df.columns)

df =df[~df['Invoice'].astype(str).str.startswith('C')]

df = df[df["Quantity"]>0]

df = df[df["Price"]>0]

df.to_csv("DataSets\FinalOnline_Retail_Data.csv")
print("Csv file creted...")
