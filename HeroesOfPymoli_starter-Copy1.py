#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[127]:


# Dependencies and Setup
import pandas as pd
import math as math
# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[128]:


purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[129]:


total_counts = purchase_data["SN"].value_counts()
total_counts.sum()


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[130]:


average_price_df = purchase_data["Price"].mean()
round(average_price_df, 2)


# In[131]:


total_purchases_df = len(purchase_data)
total_purchases_df


# In[132]:


total_revenue_df = purchase_data["Price"].sum()
total_revenue_df


# In[133]:


item_df = purchase_data.groupby("Item Name")["Item Name"].unique()
item_df.count()


# In[134]:


analysis_df = pd.DataFrame({"Number of Unique Items":[item_df.count()],
                                             "Average Purchase Price":[average_price_df],
                                            "Total Number of Purchases":[total_purchases_df],
                                             "Total Revenue":[total_revenue_df]})
analysis_df["Average Purchase Price"]=analysis_df["Average Purchase Price"].map('${:.2f}'.format)
analysis_df["Total Revenue"]=analysis_df["Total Revenue"].map('${:.2f}'.format)
analysis_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[135]:


g_count_df = purchase_data.groupby("Gender")
gender_total= g_count_df["SN"].nunique()
gender_total


# In[136]:


unique_pl = purchase_data["SN"].nunique()
g_percentage = gender_total/unique_pl*100
g_percentage


# In[137]:


g_analysis_df = pd.DataFrame({"Total Count":gender_total,
                                             "Gender Percentage":g_percentage
                                            })

g_analysis_df["Gender Percentage"]=g_analysis_df["Gender Percentage"].map('{:.2f}%'.format)
g_analysis_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[138]:


purchase_count = g_count_df['Purchase ID'].count()
purchase_count


# In[139]:


g_average_price = g_count_df["Price"].mean()
round(average_price_df, 2)


# In[140]:


gender_total = purchase_data.groupby("Gender")["Price"].sum()
gender_total


# In[143]:


gender_analysis_df = pd.DataFrame({"Purchase Count":purchase_count, 
                                   "Average Purchase Price":round(g_average_price),
                                   "Total Purchase Value": gender_total,
                                   })

gender_analysis_df


# ## Purchasing Analysis (Age)

# Establish bins for ages
# 
# 
# Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# Calculate the numbers and percentages by age group
# 
# 
# Create a summary data frame to hold the results
# 
# 
# Optional: round the percentage column to two decimal points
# 
# 
# Display Age Demographics Table
# 

# In[144]:


bins = [0,10,15,20,25,30,35,40, 45]
age_ranges = ["<10", "10-14","15-19", "20-24", "25-29", "30-34", "35-39", ">=40"]


# In[145]:


pd.cut(purchase_data["Age"], bins, labels=age_ranges)


# In[146]:


purchase_data["Age Range"] = pd.cut(purchase_data["Age"], bins, labels= age_ranges)
purchase_data.head()


# In[147]:


purchase_data.count()


# In[148]:


age_group_percent = round(purchase_data["Age Range"].value_counts()/780,2)*100
age_group_percent


# In[149]:


age_g_count = purchase_data.groupby("Age Range")["Item Name"]
age_g_count.count()


# In[150]:


age_group_aver = purchase_data.groupby("Age Range")["Price"].mean()
round(age_group_aver, 2)


# In[151]:


age_group_tl = purchase_data.groupby("Age Range")["Price"].sum()
age_group_tl


# In[152]:


aptpag_ = age_group_tl/573
round(aptpag_, 2)*100


# In[153]:


age_range_df = pd.DataFrame({"Purchase Count":age_g_count.count(),
                            "Average Purchase Price":round(age_group_aver,2),
                            "Total Purchase Value": age_group_tl,
                             "Percent of Players": aptpag_*10
})
age_range_df["Percent of Players"]=age_range_df["Percent of Players"].map('{:.2f}%'.format)
age_range_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table

# In[154]:


bins = [0,10,15,20,25,30,35,40, 45]
age_ranges = ["<10", "10-14","15-19", "20-24", "25-29", "30-34", "35-39", ">=40"]


# In[155]:


pd.cut(purchase_data["Age"], bins, labels=age_ranges)


# In[156]:


age_group_percent = round(purchase_data["Age Range"].value_counts()/780,2)*100
age_group_percent


# In[157]:


age_g_count = purchase_data.groupby("Age Range")["Item Name"]
age_g_count.count()


# In[161]:


demo_range_df = pd.DataFrame({"Purchase Count":age_g_count.count(),
                             "Percent of Players": age_group_percent
})
demo_range_df["Percent of Players"]=demo_range_df["Percent of Players"].map('{:.1f}%'.format)
demo_range_df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[162]:


players_purchase_count = purchase_data.groupby("SN").count()["Price"].rename("Purchase Count")
players_average_price = purchase_data.groupby("SN").mean()["Price"].rename("Average Purchase Price")
players_total = purchase_data.groupby("SN").sum()["Price"].rename("Total Purchase Value")


# In[164]:


total_user_data_df = pd.DataFrame({"Purchase Count":players_purchase_count,
                                   "Average Purchase Price": players_average_price,
                                   "Total Purchase Value": players_total})
total_user_data_df.head()


# In[165]:


top_spenders = total_user_data_df.sort_values("Total Purchase Value", ascending=False)
top_spenders.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[166]:


items_purchase_count = purchase_data.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")
items_average_price = purchase_data.groupby(["Item ID", "Item Name"]).mean()["Price"].rename("Average Purchase Price")
items_value_total = purchase_data.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")


# In[167]:


things_purchased_df = pd.DataFrame({"Purchase Count":items_purchase_count,
                                   "Item Price":items_average_price,
                                   "Total Purchase Value":items_value_total,})
things_purchased_df


# In[168]:


popular_items_df = things_purchased_df.sort_values("Purchase Count", ascending=False)
popular_items_df.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[169]:


profitable_items_df = things_purchased_df.sort_values("Total Purchase Value", ascending=False)
profitable_items_df.head()

