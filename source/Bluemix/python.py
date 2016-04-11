
# coding: utf-8

# In[22]:

from pyspark.sql import SQLContext
from pyspark.sql.types import *


# In[23]:

get_ipython().magic(u'matplotlib inline')


# In[24]:

followers = sqlContext.read.parquet("follow.parquet")


# In[25]:

followers.registerTempTable("followers");


# In[26]:


sqlContext.cacheTable("followers")
plt1 = sqlContext.sql("SELECT * FROM followers where followers > 100000")


# In[27]:

df1 = plt1.toPandas()
df1=df1.set_index('USER_DISPLAY_NAME')


# In[28]:


from pylab import rcParams
rcParams['figure.figsize'] = 20,10
Line=df1.plot(kind='line',title='Count by followers of users',stacked=False)
Line.set_ylabel("No.of followers in millions ") 
Line.set_xlabel("Users")


# In[42]:

hashcount = sqlContext.read.parquet("count2.parquet")


# In[43]:

hashcount.registerTempTable("hashcount");


# In[50]:


sqlContext.cacheTable("hashcount")
plt2 = sqlContext.sql("SELECT * FROM hashcount where count > 1000 limit  30")


# In[51]:

df2 = plt2.toPandas()
df2=df2.set_index('HASHTAG')


# In[53]:

from pylab import rcParams
rcParams['figure.figsize'] = 15,5
barh = df2.plot(kind='bar',title='count of tweets on HASHTAG',stacked=False)
barh.set_ylabel("No of tweets ABOUT HASHTAG") 
barh.set_xlabel("HASHTAG TOPIC") 


# In[74]:

citycount = sqlContext.read.parquet("city.parquet")


# In[75]:

citycount.registerTempTable("citycount");


# In[76]:

sqlContext.cacheTable("citycount")


# In[77]:

plt3 = sqlContext.sql("SELECT * FROM citycount")


# In[79]:

df3 = plt3.toPandas()
df3=df3.set_index('USER_CITY')


# In[135]:


from pylab import rcParams
rcParams['figure.figsize'] = 15,5
line = df3.plot(kind='line',title='count of tweets on a city',stacked=False,color='b')
line.set_ylabel("No of tweets from a city") 
line.set_xlabel("City Name") 


# In[86]:

engcount = sqlContext.read.parquet("country.parquet")


# In[87]:

engcount.registerTempTable("engcount");


# In[88]:

sqlContext.cacheTable("engcount")


# In[121]:

plt4 = sqlContext.sql("SELECT * FROM engcount WHERE ENGCOUNT>10")


# In[122]:

plt4.show()


# In[123]:

df4 = plt4.toPandas()
df4=df4.set_index('USER_COUNTRY')


# In[136]:

from pylab import rcParams
rcParams['figure.figsize'] = 15,5
barh = df4.plot(kind='bar',title='count of tweets IN ENGLISH TWEETS IN WITHOUT INDIA',stacked=False,color='k')
barh.set_ylabel("No of tweets IN ENGLISH") 
barh.set_xlabel("COUNTRY NAME") 


# In[155]:

sourcecount = sqlContext.read.parquet("sources.parquet")


# In[156]:

sourcecount.registerTempTable("sourcecount");


# In[157]:

sqlContext.cacheTable("sourcecount")


# In[164]:

plt5 = sqlContext.sql("SELECT * FROM sourcecount")


# In[165]:

plt5.show()


# In[166]:

df5 = plt5.toPandas()
df5=df5.set_index('MESSAGE_GENERATOR_DISPLAY_NAME')


# In[168]:

from pylab import rcParams
rcParams['figure.figsize'] = 15,5
area = df5.plot(kind='area',title='Sources of tweets',stacked=False)
area.set_ylabel("count") 
area.set_xlabel("sources") 


# In[4]:

hash1 = sqlContext.read.parquet("hash1.parquet")


# In[5]:

hash1.registerTempTable("hash1");


# In[6]:

sqlContext.cacheTable("hash1")
plt6 = sqlContext.sql("SELECT * FROM hash1")


# In[7]:

hash2 = sqlContext.read.parquet("hash2.parquet")


# In[8]:

hash2.registerTempTable("hash2");


# In[9]:

sqlContext.cacheTable("hash2")
plt7 = sqlContext.sql("SELECT * FROM hash2")


# In[10]:


import matplotlib.pyplot as plt
import numpy as np


# In[11]:

df6 = plt6.toPandas()
df7 = plt7.toPandas()


# In[29]:

from pylab import rcParams
rcParams['figure.figsize'] = 15, 10

fig, (ax1,ax2) = plt.subplots(1,2,sharex=True)

ax1.pie(df6['COUNTS'],labels=df6['HASHTAG'],autopct='%1.1f%%')
ax2.pie(df7['COUNTS'],labels=df7['HASHTAG'],autopct='%1.1f%%')
ax1.set_title('HASHTAGS ON TABLE WITH VIRAT KOHLI FOCUSED')
ax2.set_title('HASHTAGS ON TABLE WITH IPL FOCUSED')
plt.show()


# In[ ]:




# coding: utf-8

# In[21]:

from pyspark.sql import SQLContext
from pyspark.sql.types import *


# In[22]:

get_ipython().magic(u'matplotlib inline')


# In[23]:

sqlContext = SQLContext(sc)


# In[24]:

gender = sqlContext.read.parquet("gender.parquet")


# In[25]:

gender.registerTempTable("gender");


# In[33]:

sqlContext.cacheTable("gender")
plt1 = sqlContext.sql("SELECT * FROM gender order by 2")


# In[34]:

df1 = plt1.toPandas()
df1=df1.set_index('USER_GENDER')


# In[63]:

from pylab import rcParams
rcParams['figure.figsize'] = 15,5
barh=df1.plot(kind='barh',title='Count of  gender speaking about Dance',stacked=False,color='b')
barh.set_ylabel("Gender") 
barh.set_xlabel("tweets")


# In[42]:

senti = sqlContext.read.parquet("senti.parquet")


# In[43]:

senti.registerTempTable("senti");


# In[44]:

sqlContext.cacheTable("senti")
plt2 = sqlContext.sql("SELECT * FROM senti")


# In[46]:

senti1 = sqlContext.read.parquet("senti2.parquet")


# In[47]:

senti1.registerTempTable("senti1");


# In[48]:

sqlContext.cacheTable("senti1")
plt3 = sqlContext.sql("SELECT * FROM senti1")


# In[49]:

import matplotlib.pyplot as plt
import numpy as np


# In[50]:

df2 = plt2.toPandas()
df3 = plt3.toPandas()


# In[59]:


from pylab import rcParams
rcParams['figure.figsize'] = 15, 10

fig, (ax1,ax2) = plt.subplots(1,2,sharex=True)

ax1.pie(df2['counts'],labels=df2['USER_GENDER'],autopct='%1.1f%%')
ax2.pie(df3['counts'],labels=df3['USER_GENDER'],autopct='%1.1f%%')
ax1.set_title('Analysis on sentiment for like or love')
ax2.set_title('Analysis on sentiment for hate or anger')
plt.show()

