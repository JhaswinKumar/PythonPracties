import pandas as pd

# df1 = pd.read_excel("DataSets\online_retail_II.xlsx",sheet_name='Year 2009-2010',engine='openpyxl')
# df2 = pd.read_excel("DataSets\online_retail_II.xlsx",sheet_name='Year 2010-2011',engine='openpyxl')


# df =pd.concat([df1,df2],ignore_index=True) #ignore_index it will start with again 0 onwards

# print(df.shape)
# print(df.columns)

# print(df.info())
# print(df.describe())

# ##Cleaning & Feature Engineering
# df.dropna(subset=['InvoiceDate','Customer ID'],inplace= True)

# print(df.shape)
# print(df.columns)

# df =df[~df['Invoice'].astype(str).str.startswith('C')]

# df = df[df["Quantity"]>0]

# df = df[df["Price"]>0]

# df.to_csv("DataSets\FinalOnline_Retail_Data.csv")
# print("Csv file creted...")

df =pd.read_csv("DataSets\FinalOnline_Retail_Data.csv")
print(df.shape)
print(df.columns)
## Add new Features
df['Revenue'] =df['Quantity'] * df['Price'] # feature engineering
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)  # feature engineering
#2009-01
#2009-03

print(df.head())

#make monthwise invoice

monthly_revenue = df.groupby('Month')['Revenue'].sum().sort_index()

print(monthly_revenue)
print(monthly_revenue.index)
print(monthly_revenue.values)
print(type(monthly_revenue))
#Create matplotlib
# matplotlib  -->  seaborn,pandas plot

import matplotlib.pyplot as plt

#Line plot

plt.figure(figsize=(16,8))

print(plt.style.available)

# plt.plot(monthly_revenue.index,monthly_revenue.values,marker ='o') #o means circle
# plt.xlabel("Year - Months")
# plt.ylabel("Revenue")
# plt.title('Revenue in Months')
# plt.xticks(rotation =45) # x-axis label rotation
# plt.grid(True) # it will show grid lines in diagram
# plt.style.use('classic') #use different styles of graphs
# plt.savefig("Images\MonthlyRevenue1.png",dpi=300)
# plt.show()


################################################################################


# plt.plot(monthly_revenue.index,monthly_revenue.values,marker ='o') #o means circle

# for i,value in enumerate(monthly_revenue):
#     plt.text(monthly_revenue.index[i],value,f"{int(value):,}",ha='center',fontsize=8)
# plt.xlabel("Year - Months")
# plt.ylabel("Revenue")
# plt.title('Revenue in Months')
# plt.xticks(rotation =45) # x-axis label rotation
# plt.grid(False) # it dont show grid lines in diagram
# plt.style.use('ggplot') #use different styles of graphs
# plt.savefig("Images\MonthlyRevenue_ggplotstyle.png",dpi=300)
# plt.show()


#################################################################################
fontstyle ={

    'family' : 'serif',
    'color'  : 'red',
    'weight' : 'bold',
    'size'   : 8
}
plt.plot(monthly_revenue.index,monthly_revenue.values,marker ='o',c='green') #o means circle

for i,value in enumerate(monthly_revenue):
    plt.text(monthly_revenue.index[i],value,f"{int(value):,}",ha='right',fontdict=fontstyle)
plt.xlabel("Year - Months")
plt.ylabel("Revenue")
plt.title('Revenue in Months')
plt.xticks(rotation =45) # x-axis label rotation
plt.grid(False) # it dont show grid lines in diagram
plt.style.use('ggplot') #use different styles of graphs
plt.savefig("Images\MonthlyRevenue_fontdict.png",dpi=300)
plt.show()

## Show top 10 revenue generating countries
country_revenue = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10) #big value to small value
print(country_revenue)
country_revenue1= df.groupby('Country')['Revenue'].sum().sort_values(ascending=True).head(10) # small value to big value
print(country_revenue1)


plt.bar(country_revenue.index,country_revenue.values,color='orange')
plt.xlabel("Year - Months")
plt.ylabel("Revenue")
plt.title('Revenue in Months')
plt.xticks(rotation =45) # x-axis label rotation
plt.tight_layout() # used to remove padding
plt.savefig("Images\MonthlyRevenue_BarChart.png",dpi=300)
plt.show()


#############################################################################



plt.barh(country_revenue.index,country_revenue.values,color='orange')
plt.xlabel("Year - Months")
plt.ylabel("Revenue")
plt.title('Revenue in Months')
plt.xticks(rotation =45) # x-axis label rotation
plt.tight_layout() # used to remove padding
plt.savefig("Images\MonthlyRevenue_BarhChart.png",dpi=300)
plt.show()

################################################

plt.bar(country_revenue.index,country_revenue.values,color='#BE398D') # with hex color
plt.xlabel("Year - Months")
plt.ylabel("Revenue")
plt.title('Revenue in Months')
plt.xticks(rotation =45) # x-axis label rotation
plt.tight_layout() # used to remove padding
plt.savefig("Images\MonthlyRevenue_BarChart.png",dpi=300)
plt.show()
