
In [ ]:


1.import numpy as np 
2.import pandas as pd 
3.import matplotlib.pyplot as plt




In [ ]:


1.import os
2.for dirname, _, filenames in os.walk('/kaggle/input'):
3.for filename in filenames:
4.print(os.path.join(dirname, filename))




In [ ]:


1.df=pd.read_table('drugsComTrain_ra.tsv')
2.df




In [ ]:


1.df.shape




In [ ]:


1.def sentiment(df):
2.df.loc[df.rating<4,'Sentiment']="Negative"
3.df.loc[(df.rating>=4) & (df.rating<7) ,'Sentiment']="Neutral"
4.df.loc[(df.rating>=7),'Sentiment']="Positive"
5.return df




In [ ]:


1.df=sentiment(df)




In [ ]:


1.df.loc[df.Sentiment=='Negative',['rating']].head(20)




In [ ]:


1.df['drugName'].value_counts()




In [ ]:


1.plt.hist(df['rating'])
2.plt.xlabel("Ratings")
3.plt.ylabel("No.of reviews")
4.plt.title("Ratings vs No.of reviews")




In [ ]:


1.df.head()




In [ ]:


1.df=df.drop(['uniqueID','drugName','condition','date','usefulCount'],axis=1)




In [ ]:


1.df.head()


In [ ]:

1.import nltk
2.from nltk.corpus import stopwords
3.from nltk.stem.snowball import SnowballStemmer
4.from nltk import word_tokenize
5.from nltk.corpus import stopwords 

In [ ]:


1.def prepro(df):
2.tokens=word_tokenize(df)
3.stemmer=SnowballStemmer('english',ignore_stopwords=True)
4.stemmed=[stemmer.stem(word) for word in tokens]
5.words=[word for word in stemmed if word.isalpha()]
6.stop_words=set(stopwords.words('english'))
7.st=[w for w in words if not w in stop_words]
8.return st




In [ ]:


1
df['review']=df.apply(lambda row:prepro(row['review']),axis=1)




In [ ]:




1
X=df.drop('Sentiment',axis=1)
2
y=df['Sentiment']
3
X.shape
4
y.shape









