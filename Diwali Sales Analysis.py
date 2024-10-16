#!/usr/bin/env python
# coding: utf-8

# # Diwali Sales Analysis

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r"C:\Users\nibed\Downloads\Diwali Sales Data.csv", encoding= 'unicode_escape')
df


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


# Check for null values
pd.isnull(df).sum()


# In[8]:


# Drop null values
df.dropna(inplace=True)


# In[9]:


# Change data type
df['Amount'] = df['Amount'].astype('int')


# In[10]:


df['Amount'].dtypes


# In[11]:


df.columns


# In[12]:


#rename column
df.rename(columns= {'Age Group':'Age_Group'})


# In[13]:


df.describe()


# In[14]:


# Use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# ### Gender

# In[15]:


# Plotting a Bar Chart for Gender and it's count
plt.figure(figsize=(7, 3))
ax = sns.countplot(data = df, y = 'Gender', color = '#94fc03')

# Adding labels to the bars
for container in ax.containers:
    ax.bar_label(container, rotation=90, 
                 color='#026117', fontsize=15, fontweight = 'bold')


# - <p style="color:purple; font-size:17px;">
#     <b style="color:green;">Count Plot</b> in Seaborn is the same as a 
#     <b style="color:green;">Bar Chart</b> in Matplotlib. 
#     <b style="color:green;">ax</b> counts the occurrences of each category in the 
#     <b style="color:green;">Gender</b> column and plots them.
# </p>
#     
# - <p style="color:purple; font-size:17px;">The loop iterates over each bar container in the plot. 
#     <b style="color:#055917; background-color:#c7f2d0">ax.bar_label(bars)</b> adds the count as a label on top of each bar.</p>
# 
# - <p style="color:purple; font-size:17px;">Using 
#     <b style="color:#055917; background-color:#c7f2d0">sns.countplot</b>, the code counts how many times 'Male' and 'Female' appear in the dataset and plots those counts. Adding the labels helps identify the exact count of each category directly on the chart. </p>

# In[16]:


# Plotting a Bar Chart for Gender and it's count
plt.figure(figsize=(7, 3))
ax_gen = sns.countplot(data = df, y = 'Gender', color = '#94fc03')

# Adding labels to the bars
for container in ax_gen.containers:
    ax_gen.bar_label(container, label_type='center',
                 color='#026117', fontsize=15, fontweight = 'bold')


# - <b style="color:purple; font-size:17px;">So, most of the buyers are females.</b>

# In[17]:


# plotting a bar chart for gender vs total amount

sales_by_gen = df.groupby(['Gender'], 
                       as_index=False)['Amount'].sum().sort_values(
    by='Amount', ascending=False)
sales_by_gen


# In[18]:


df.groupby('Gender', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[19]:


plt.figure(figsize=(7, 3))
sns.barplot(data = sales_by_gen, x = 'Gender', y= 'Amount', color = '#94fc03')
plt.show()


# - <b style="color:purple; font-size:17px;">The purchasing power of the females are greater than the males.</b>

# ### Age

# In[21]:


plt.figure(figsize=(8, 4))
ax_age = sns.countplot(data = df, x = 'Age Group', 
                       hue = 'Gender', palette = 'light:g')

for bars in ax_age.containers:
    ax_age.bar_label(bars)


# <div style="color:purple;
#           padding:8px; 
#           border:2px solid green;
#           background-color:#ecfce6;
#           font-size:17px;
#           max-width:600px;">
#     <ul>
#         <li>We can also experiment with different palettes like 
#     <b style="color:green;">deep</b>, 
#     <b style="color:green;">muted</b>, 
#     <b style="color:green;">bright</b>, 
#     <b style="color:green;">pastel</b>, 
#     <b style="color:green;">dark</b>, and 
#     <b style="color:green;">colorblind</b>.
#         </li>
#         <li>But I prefer custom colors. So, I'll specify my own palette.</li>
#     </ul>
# </div>

# In[22]:


plt.figure(figsize=(8, 4))
ax_age = sns.countplot(data = df, x = 'Age Group', 
                       hue = 'Gender', palette = ['green', 'yellow'])

for bars in ax_age.containers:
    ax_age.bar_label(bars)


# In[23]:


# Total Amount vs Age Group
sales_by_age = df.groupby(['Age Group'], 
                       as_index=False)['Amount'].sum().sort_values(
    by='Amount', ascending=False)

plt.figure(figsize=(8, 4))
sns.barplot(data = sales_by_age, x = 'Age Group', y = 'Amount', color = '#96ff03')
plt.show()


# - <b style="color:purple; font-size:17px;">Most of the buyers are of age group between 26-35 yrs females.</b>

# ### State

# In[31]:


# Total number of Orders from top 8 States
orders_by_state = df.groupby(['State'], 
                            as_index=False)['Orders'].sum().sort_values(
    by='Orders', ascending=False).head(8)

sns.set(rc = {'figure.figsize':(15, 5)})
sns.barplot(data = orders_by_state, x = 'State', y = 'Orders', color = '#96ff03')
plt.show()


# In[32]:


# Total Amount/Sales from top 8 States
sales_by_state = df.groupby(['State'], 
                            as_index=False)['Amount'].sum().sort_values(
    by='Amount', ascending=False).head(10)

sns.barplot(data = sales_by_state, x = 'State', y= 'Amount', color = '#96ff03')
plt.show()


# - <b style="color:purple; font-size:17px;">Most of the orders & total sales are from Uttar Pradesh, Maharashtra and Karnataka respectively.</b>

# In[90]:


# Resetting Seaborn settings to default
sns.reset_defaults()


# In[43]:


plt.figure(figsize=(8, 3))
sns.barplot(data = sales_by_state.head(), x = 'State', y = 'Amount', color = '#96ff03')
plt.show()


# ### Marital Status

# In[70]:


plt.figure(figsize=(7, 3))
ax_mar_sta = sns.countplot(data = df, y = 'Marital_Status', color = '#96ff03')

for bars in ax_mar_sta.containers:
    ax_mar_sta.bar_label(bars, label_type='center')
    
plt.show()


# In[100]:


# Sales by Marital_Status
sales_by_state = df.groupby(['Marital_Status', 'Gender'],
                            as_index=False)['Amount'].sum().sort_values(
    by='Amount', ascending=False)

plt.figure(figsize=(8, 3))
sns.barplot(data = sales_by_state, x = 'Marital_Status', y = 'Amount', 
            hue = 'Gender', palette = ['green', 'yellow'])
plt.show()


# - <b style="color:purple; font-size:17px;">Most of the buyers are married (women) and they have high purchasing power.</b>

# ### Occupation

# In[105]:


plt.figure(figsize=(20, 5))
ax_occu = sns.countplot(data = df, x = 'Occupation', color = '#96ff03')

for bars in ax_occu.containers:
    ax_occu.bar_label(bars)
    
plt.xlabel("Occupation", size = 20)
plt.ylabel("Count", size = 20)
plt.show()


# In[118]:


# Sales by Occupation
sales_by_occu = df.groupby(['Occupation'], 
                         as_index=False)['Amount'].sum().sort_values(
    by='Amount', ascending=False)

plt.figure(figsize=(20, 5))
sns.barplot(data = sales_by_occu, x = 'Occupation', y = 'Amount', color = '#96ff03')

plt.title("Sales by Occupation", size = 25)
plt.xlabel("Occupation", size = 20)
plt.ylabel("Amount", size = 20)
plt.show()


# - <b style="color:purple; font-size:17px;">Most of the buyers are working in IT, Healthcare and Aviation sector.</b>

# ### Product Category

# In[117]:


plt.figure(figsize=(20, 5))
ax_prod_cat = sns.countplot(data = df, x = 'Product_Category', color = '#96ff03')

for bars in ax_prod_cat.containers:
    ax_prod_cat.bar_label(bars)
    
plt.show()


# In[123]:


# Sales Product Category
sales_by_prod_cat = df.groupby(['Product_Category'], 
                             as_index=False)['Amount'].sum().sort_values(
    by='Amount', ascending=False).head(10)

plt.figure(figsize=(20, 6))
sns.barplot(data = sales_by_prod_cat, x = 'Product_Category', y = 'Amount', color = '#96ff03')

plt.title("Sales by Product Category", size = 25)
plt.xlabel("Product Category", size = 20)
plt.ylabel("Amount", size = 20)
plt.show()


# - <b style="color:purple; font-size:17px;">Most of the sold Products are from 
#     <b style="color:green">Food</b>, 
#     <b style="color:green">Clothing and Electronics</b> and 
#     <b style="color:green">Electronics and Gadgets</b> category.</b>

# In[129]:


# Orders Product Category
orders_by_prod_cat = df.groupby(['Product_ID'], 
                         as_index=False)['Orders'].sum().sort_values(
    by='Orders', ascending=False).head(10)

plt.figure(figsize=(15, 5))
sns.barplot(data = orders_by_prod_cat, x = 'Product_ID', y = 'Orders', color = '#96ff03')

plt.title("Orders by Product Category", size = 20)
plt.xlabel("Product Category", size = 15)
plt.ylabel("Orders", size = 15)
plt.show()


# In[137]:


# Top 10 most sold Products (same as above)

fig1, ax1 = plt.subplots(figsize=(15, 5))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(
    kind='bar', color = '#05750a')

plt.show()


# In[155]:


# Top 5 most sold Products

plt.figure(figsize=(7, 3))
df.groupby('Product_ID')['Orders'].sum().nlargest(5).sort_values(ascending=False).plot(
    kind='barh', color = '#05750a')

plt.show()


# ## Conclusion
# 
# - <b style="color:purple;">Women who are
#     <b style="color:green">Married</b> of age group 
#     <b style="color:green">26-35</b> yrs from 
#     <b style="color:green">UP</b>, 
#     <b style="color:green">Maharastra</b> and 
#     <b style="color:green">Karnataka</b> working in 
#     <b style="color:green">IT</b>, 
#     <b style="color:green">Healthcare</b> and 
#     <b style="color:green">Aviation</b> are more likely to buy products from 
#     <b style="color:green">Food</b>, 
#     <b style="color:green">Clothing and Electronics</b> and 
#     <b style="color:green">Electronics and Gadgets</b> category.</b>

# In[ ]:




