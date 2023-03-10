#!/usr/bin/env python
# coding: utf-8

# # Nifty Fifty Stock Analysis

# # Introduction

# #### This Data sets include information about the Nifty Fifty stocks in National Stock Exchange market in India and I choose the Adani Ports stock and Explore the analysis using matplotlip and seaborn library

# In[1]:


#Import all the dependecies in this project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
color_pal = sns.color_palette()
import warnings


# In[2]:


#Read the dataset
stock=pd.read_csv('ADANIPORTS.csv')


# In[3]:


#view the dataset
stock


# ## Visual and programmatic Assesment

# In[4]:


#Check the shape of data
stock.shape


# ###### The dataset has 3299 rows and 16 columns 

# In[5]:


#check the column info and information
stock.info()


# ###### From the above dataset has the following issuses

# * Missing/ Null Values 

# Trades

# In[6]:


#Dropping the unneccessary column

stocks=stock.drop(['Trades','%Deliverble','Series','Prev Close'],axis='columns')


# In[7]:


stocks


# In[8]:


#Change the datatype
stocks['Date']=pd.to_datetime(stocks['Date'])


# In[ ]:





# In[9]:


#view the dataset
stocks


# In[10]:


#Check the null values in the dataset
stocks.isnull().sum()


# *After fixing the missing values , will drop the columns that is not using this project 

# In[11]:


#After cleaning data check the info of table
stocks.info()


# In[12]:


#check the dimension of the table
stocks.shape


# *Saving a copy of  cleaned data

# In[13]:


#save the data
stocks.to_csv('stocks.csv',index=False)


# *Here i am using another one data , that is called Metadata the dataset shows the different sectors in the stock market 
# and what are the companies investing in which sector

# In[14]:


#load the dataset
metadata=pd.read_csv('stock_metadata.csv')


# In[15]:


#view the dataset
metadata.head(5)


# In[16]:


#check the dimension of the table
metadata.shape


# In[17]:


#drop the unnecssary columns
metadatas=metadata.drop(['Series','ISIN Code'],axis='columns')


# In[18]:


#view the dataset
metadatas


# ## Questions

# 1.Which Companies are investing Which Sector Stocks

# 2.Display industry sectors and Companys
# 

# 3.Plot the graph to Visualize the Trending Price of Adani Port Stock
# 

# 4.Plot 100 Days moving Average
# 

# 5.Plot the difference between 100 and 200 Days moving Average
# 

# 6.Adani port Volume of trade in 2008-2021
# 

# 7.Find the average of High,Low,Open,Close in 2019-2021
# 

# 8.check which day adani port trade max trading volume
# 

# 9.Find the Intraday Volume of Trade Per Day
# 

# 10.plot Different types of volume trades in adani stocks
# 

# 11.Top 5 high volume trades in adani stocks
# 

# 12.Find the average monthly Open of adani Port
# 

# 13.Finding Last Business day for every month
# 
# 

# 14.Get the last business day of each Quarter from April-2019

# ## Exploration

# ### Which Companies are investing Which Sector Stocks?

# In[19]:


plt.figure(figsize=(16,6))
sns.countplot(metadatas['Industry'],color="b")
plt.title('Sector Wise Companies investing')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.show()


# Majority of the sector is Financial Services and Energy sector ,
# Most of the MNC's are investing these two sectors

# There are 13 sectors in Nifty-50 Stocks
# 
# The top trading companies are listed in Each Sector
# 
# So that We have a good understanding idea to invest our money in  which sector

# ### Display industry sectors and Companys

# In[20]:


ab=metadatas.iloc[:,[1,0]]
ab.sort_values(by='Industry')


# ### Plot the graph to Visualize the Trending Price of Adani Port Stock

# In[21]:


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(17,15))

# Plot open price on first subplot
stocks.plot(ax=ax1, x='Date', y='Open', color='g')
ax1.set_xlabel("Date")
ax1.set_ylabel("Price range")
ax1.set_title("Open VS Date")

# Plot close price on second subplot
stocks.plot(ax=ax2, x='Date', y='Close', color='r')
ax2.set_xlabel("Date")
ax2.set_ylabel("Price range")
ax2.set_title("Close VS Date")

plt.tight_layout()
plt.show()


# ### Plot 100 Days moving Average

# In[22]:


#use rolling command into take the 100 days average value 
ma100=stocks.Open.rolling(100).mean()


# In[23]:


#View
ma100


# This is showing first 100 values as NAN values after that it takes the avearage of every 100 to 100.

# In[24]:


plt.figure(figsize=(15,10))
plt.plot(stocks.Open,label="Open")
plt.plot(ma100,label="ma100")
plt.legend()
plt.show()


# Importance of a 100-day Moving Average A moving average over 100 days helps investors see how the stock has performed over 20 weeks and to find the price trend if it is upward or downward

# ### Plot the difference between 100 and 200 Days moving Average

# In[90]:


#Plot-the-difference-between-100-and-200-Days-moving-Average 
ma200=stocks.Open.rolling(200).mean()


# In[26]:


#view the data
ma200


# In[36]:


plt.figure(figsize=(15,10))
plt.plot(stocks.Open,label="Open")
plt.plot(ma100,label="ma100")
plt.plot(ma200,label="ma200")
plt.title('Difference between 100 and 200 Days moving Average')
plt.legend()
plt.show()


# The difference between a 100-day moving average and a 200-day moving average is the amount of data that is being used to calculate the average. Because the 200-day moving average is based on twice as much data as the 100-day moving average, it will be less sensitive to short-term fluctuations and changes in the stock's price. It is considered as a long-term indicator, looking at the average trend of price over a longer period.

# ### Adani port Volume of trade in 2008-2021

# In[29]:


#create a Duplicate dataset
stocksdate=stocks


# In[73]:


#Assign the start date and end date to these variable and access
start_date = "2019-04-30"
end_date = "2021-04-30"
mask=(stocksdate["Date"] >= start_date) & (stocksdate["Date"] <= end_date)
stocksdate=stocksdate.loc[mask]


# In[ ]:





# In[57]:


plt.figure(figsize=(15,8))
plt.plot(stocksdate['Volume'])
plt.title("Adani port Volume of trade in 2019-2021")
plt.ylabel('Volume in Crores')
plt.show()


# In[56]:


max_volume=max(stocksdate['Volume'])
max_row=stocksdate.loc[stocksdate['Volume'] == max_volume]
max_row


# The Volume of trade happend in the adani ports between 2008- 2021 . The Highest Volume of trade is 5.2 Crore Volume Trade is this day and the date is 13 April 2021

# ### Find the average of High,Low,Open,Close in 2019-2021

# In[66]:


#find the average 
avghigh=stocksdate["High"].mean()
avglow=stocksdate["Low"].mean()
avgopen=stocksdate["Open"].mean()
avgclose=stocksdate["Close"].mean()

print("Adani Port Average high:",avghigh,
      "\nAdani Port Average Low:",avglow,
      "\nAdani Port Average Open:",avgopen,
      "\nAdani Port Average Close:",avgclose)


# ### Find the Intraday Volume of Trade Per Day

# In[74]:


#To find the intraday volume is to subtract the Volume into Deliverable Volume
stocks["Intraday Volume"]=stocks['Volume']-stocks["Deliverable Volume"]
stocks.head()


# In this Process i add one column to find the intraday volume of trade

# ### Plot Different types of volume trades in adani stocks

# In[76]:


#Plot the Piechart
plt.figure(figsize=(8,8))
DVIV=["Deliverable Volume","Intraday Volume"]
piechart=stocks["Deliverable Volume"].sum(),stocks["Intraday Volume"].sum()
plt.pie(piechart,labels=DVIV,autopct="%1.2f%%")
plt.title("Types of Volumes in Adani Port Stocks")
plt.show()


# In this Pie chart Display the deliverable volume and intraday volume of trade per day the most of the people are doing intraday trading only, so adani port stock is more volatile so most of all investing intraday Volume

# ### Top 5 high volume trades in adani stocks

# In[79]:


Top_5=stocks.sort_values(by="Volume",ascending=False)
Top_5.head()


# ### Find the average monthly Open of adani Port

# In[87]:


#Assume new Variable
stockdates=stocksdate
stockdates=stockdates.set_index('Date')
stockavg.head()


# In[88]:


stockdates.Open.resample("M").mean()


# ### Finding Last Business day for every month

# In[91]:


stockdates1=stockdates.resample("M").last()
stockdates1


# ### Get the last business day of each Quarter from April-2019

# In[93]:


#Find the quarterly date
stockdates1.resample("Q").last()


# In[ ]:




