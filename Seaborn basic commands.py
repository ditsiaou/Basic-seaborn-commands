#!/usr/bin/env python
# coding: utf-8

# In[1]:


path='C:/Users/ditsi/Desktop/python/Understanding and Visualising Data with Python/Cartwheeldata.csv'


# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 100)


# In[3]:


df = pd.read_csv(path)
print(df.head())


# In[4]:


sns.scatterplot( data=df,x="Wingspan", y="CWDistance")
# a simple scatterplot with sns.scatterplot


# In[5]:


sns.scatterplot( data=df,x="Wingspan", y="CWDistance", hue="Gender")
# Scatterplot like the previous where hue is grouping the data by Gender


# In[6]:


sns.barplot( data=df,x="Glasses", y="CWDistance",hue='Gender')
# a barplot with sns.barplot


# In[7]:


sns.barplot(y=df["Glasses"], x=df["CWDistance"],hue=df['Gender'])
# instead of introducing orient='h' like in a next boxplot we change the x and y of previous diagram


# In[8]:


sns.boxplot(x= df['Glasses'], y=df['Height'])
# a basic box/whisker  plot


# In[9]:


sns.boxplot(x= 'Glasses', y='Height',data=df)
# this and the previous are actually the same. In the previous we see how to not insert data= something pr\arameter.


# In[10]:


sns.boxplot(x= 'Glasses', y='Height',data=df,hue='Gender')
# grouping the previous box plot by Gender 


# In[11]:


sns.boxplot(y= 'Glasses', x='Height',data=df,hue='Gender')
# exchanging the axis to simply produce an horizontal box plot


# In[12]:


sns.boxplot(data=df,orient='h')


# In[13]:


sns.histplot(x=df["Height"])
# producing a simple histogram
# histogram is better for continuous variables in x-axis


# In[14]:


sns.distplot(x=df["Height"])
#not suggested as you see


# In[15]:


sns.catplot(data=df, kind="swarm", x="Gender", y="CWDistance", hue="Glasses")


# In[16]:


sns.catplot(data=df, kind="violin", x="Gender", y="CWDistance", hue="Glasses")


# In[17]:


sns.catplot(data=df, kind="violin", x="Gender", y="CWDistance", hue="Glasses",split=True)


# In[18]:


sns.catplot(data=df, kind="violin", x="Gender", y="CWDistance", hue="Glasses",split=False)
#same as the diagram without split


# In[ ]:





# In[ ]:




