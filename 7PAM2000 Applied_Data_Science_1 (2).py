
#import relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load csv file via pandas read_csv() function
df = pd.read_csv('SampleSuperstore.csv')

#using pandas pivot table function to find total sales per category
table = pd.pivot_table(data=df, index ='Category',values ='Sales', aggfunc=np.sum)

#Plotting barchart of aggregate sales across product categories
fig, ax = plt.subplots()
category = table.index
sales = table['Sales']
bar_labels =['Furniture','Office Supplies', 'Technology']
ax.bar(category,sales,label=bar_labels,width=0.5)
ax.set_ylabel('Sales')
ax.set_xlabel('Category')
ax.set_title('Barchart showing sales across categories')

plt.show()

#Plotting pie chart to percentage of profit across segment

#using pandas pivot table function to find total sales across segment
table_1 = pd.pivot_table(data=df, index='Segment', values='Profit', aggfunc=np.sum)
fig, ax = plt.subplots()
Segment = table_1.index
profit = table_1['Profit']
colors = plt.get_cmap('Oranges')(np.linspace(0.2, 0.7, len(profit)))
explode = (0,0.1,0)
pie_labels =['Consumer', 'Corporate', 'Home Office']
ax.pie(profit,explode=explode, labels=pie_labels, colors=colors, autopct='%1.1f%%', shadow=True,startangle=90,
       wedgeprops={"linewidth": 1, "edgecolor": "black"}, frame=False)
ax.set_title('Pie chart showing percentage profit across segment')
ax.legend(title = 'Segment', loc='lower left', bbox_to_anchor= (0.0, -0.1), ncol=3,
            borderaxespad=0, frameon=False)
plt.show()

#making line plots from aggregate of sales made across categories and profit across segment
pivot = pd.pivot_table(df,index='Region', values='Profit', aggfunc=np.sum)
pivot1 = pd.pivot_table(df, index='Region', values='Sales', aggfunc=np.sum)
#pivot2 = pd.pivot_table(df, index='Sub-Category', values='Sales', aggfunc=np.sum)

Region = pivot.index
profit_region = pivot['Profit']
sales_region = pivot1['Sales']

fig, ax = plt.subplots()
ax.plot(Region,profit_region, Region, sales_region)
ax.set_xlabel('Region')
ax.legend(["Total Profit", "Total Sales"], loc ="best")
ax.set_title('Plot of total profit and total sales across region')
plt.show()


