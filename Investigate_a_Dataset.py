#!/usr/bin/env python
# coding: utf-8

# 
# # Project: Investigate No_showAppointments Dataset  
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 

# In[2]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html
get_ipython().run_line_magic('matplotlib', 'inline')


# In[1]:


5 != 6


# <a id='wrangling'></a>
# ## Data Wrangling
# 

# In[3]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df = pd.read_csv("noshowappointments-kagglev2-may-2016.csv")
df.head()


# In[4]:


df.shape


# #### The data has 110527 rows and 14 columns 

# In[5]:


df.describe()


# The mean of ages is 37 years old
# 
# The oldest patient is 115 years old
# 
# The youngest patient is -1 ( We will fix this later as it doesn't make sense )

# # Checking for missing values

# In[6]:


df.isnull().sum()


# ###### There is no missing values

# 
# ## Data Cleaning 

# In[7]:


df[df.Age == -1]


# In[8]:


df.drop(99832,inplace = True)


# In[9]:


df[df.Age == -1]


# In[10]:


df.describe()


# ###### Now the youngest patient is 0 years old 

# In[11]:


# Renaming columns to be easy to use 
df.rename(columns = {'Hipertension' : 'Hypertension'} , inplace = True)
df.rename(columns = {'No-show' : 'No_show'},inplace = True)


# In[12]:


df.head()


# ##### Removing columns which we won't use

# In[13]:


df.drop(columns = ['PatientId','AppointmentID'] , inplace = True)


# In[14]:


df.head()


# In[15]:


## chaning type of (ScheduledDay ,AppointmentDay ) to datetime 
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'] )
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'] )


# In[16]:


df['Time_differnce'] = df['AppointmentDay'] - df['ScheduledDay']


# In[17]:


df.head()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 

# ### General investigating for the data

# In[18]:


df.hist(figsize = (15,15) , alpha = 0.8 , color = 'red');


# - Most of the patients aren't in the scholarship 
# 
# - Most of the patients aren't alcoholic 
# 
# - Most of the patients don't have handcap , Hypertension or diabetes 
# 
# - Most of the patients didn't receive a sms message 
# 
# - Most of the patients age from 0 to 20 years 

# ## Does the Neighbourhood affect the number of people who show ?

# In[19]:


show = df.No_show == 'No'
noshow = df.No_show == "Yes"


# In[20]:


plt.figure(figsize = (18,8))
df.Neighbourhood[show].value_counts().plot(kind = 'bar' , color = 'red',  label = 'Number of people show' )
df.Neighbourhood[noshow].value_counts().plot(kind = 'bar', color = 'blue', label = 'Number of people didn\'t show')
plt.legend()
plt.title('No of people who show to number of people who didn\'t from different Neighbourhoods')
plt.xlabel('Neighbourhood')
plt.ylabel('Number of patients');


# - ###### It seems that neighbourhood affect the number of people who show as there is a great difference between different deighbourhoods

# ## Does the SMS affect the number of people who show ?

# In[21]:


plt.figure(figsize = (10,10))
df.SMS_received[show].value_counts().plot(kind = 'bar' , color = 'red',  label = 'Number of people show' )
df.SMS_received[noshow].value_counts().plot(kind = 'bar', color = 'blue', label = 'Number of people didn\'t show')
plt.legend()
plt.title('No of people who show to number of people who didn\'t for those who received as SMS')
plt.xlabel('Sms Received')
plt.ylabel('Number of patients');


# - ###### The sent SMS's doesn't seem to play a great role in reminding them as most of the people show up without receiving any sms 

# ## Does the age affect number of people who show ?

# In[22]:


plt.figure(figsize = (10,10))
df.Age[show].plot(kind='hist', color = 'red',  label = 'Number of people show' )
df.Age[noshow].plot(kind='hist', color = 'blue', label = 'Number of people didn\'t show')
plt.legend()
plt.title('No of people who show to number of people who didn\'t from different ages')
plt.xlabel('Age')
plt.ylabel('Number of patients');


# - ###### Most of people show range from 0 to 10 years old
# - ###### Most of the old age don't seem to show  up alot compared to young age and it makes sense 

# ## Is there a big gap between males and females at showing up ?

# In[44]:


df.groupby(['Gender'])['Age'].count().plot(kind = 'bar',color=['red','blue'] ).set_ylabel('Number of patients');
df.groupby(['Gender'])[['Age']].count()


# - ###### Females show up more than men but this also makes sense as 64% of the patients are females 

# ## Does the scholarship affect the number of people who show up ?

# In[51]:


plt.figure(figsize = (10,10))
df.Scholarship[show].value_counts().plot(kind = 'bar' , color = 'red',  label = 'Number of people show' )
df.Scholarship[noshow].value_counts().plot(kind = 'bar', color = 'blue', label = 'Number of people didn\'t show')
plt.legend()
plt.title('No of people who show to number of people who didn\'t for those who has a scholarship')
plt.xlabel('The scholarship')
plt.ylabel('Number of patients');


# - ###### The scholarship doesn't seem to have alot of influence on people 

# <a id='conclusions'></a>
# # Conclusions
# ###### After this visualization we can conclude that :
# - The SMS's aren't really that important and i think you should stop sending it                                              
# - they look after their childern so much as we can see the most show age is from 0 to 10 years old
# - The neighbourhood plays an important role at the number of patients who showed up as there is a remarkable difference between different neighbourhoods
# - As people grow old they don't show up alot compared to young age 
# - The scholarship doesn't seem to make a great difference 
# 

# In[52]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




