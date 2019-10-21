#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("drugsComTrain_raw.tsv",delimiter='\t')
df2=pd.read_csv("drugsComTest_raw.tsv",delimiter='\t')


# In[3]:


df.rename(columns={'Unnamed: 0':'UniqueId'},inplace=True)
df2.rename(columns={'Unnamed: 0':'UniqueId'},inplace=True)


# In[4]:


df2['review'][10]


# In[5]:


df['review'][10]


# In[7]:


df=df.drop(['UniqueId','drugName','condition','date','usefulCount'],axis=1)
df2=df2.drop(['UniqueId','drugName','condition','date','usefulCount'],axis=1)


# In[8]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer,PorterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords 


# In[9]:


def prepro(df):
    tokens=word_tokenize(df)
    stemmer=SnowballStemmer('english',ignore_stopwords=True)
    stemmed=[stemmer.stem(word) for word in tokens]
    words=[word for word in stemmed if word.isalpha()]
    stop_words=set(stopwords.words('english'))
    st=[w for w in words if not w in stop_words]
    return st


# In[11]:


df['review']=df.apply(lambda row:prepro(row['review']),axis=1)


# In[10]:


df2['review']=df.apply(lambda row:prepro(row['review']),axis=1)


# In[12]:


X=df.drop('rating',axis=1)
y=df['rating']


# In[14]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42,stratify=y)


# In[15]:


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
train_Xv=vectorizer.fit_transform(X_train['review'].astype(str))
test_Xv=vectorizer.transform(X_test['review'].astype(str))
train_Xv.shape

