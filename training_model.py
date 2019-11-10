#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer,PorterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import seaborn as sns
from sklearn.neural_network import MLPClassifier


# In[6]:


df=pd.read_csv("drugsComTrain_raw.tsv",delimiter='\t')
df2=pd.read_csv("drugsComTest_raw.tsv",delimiter='\t')


# In[8]:


df.rename(columns={'Unnamed: 0':'UniqueId'},inplace=True)
df2.rename(columns={'Unnamed: 0':'UniqueId'},inplace=True)


# In[9]:


plt.hist(df['rating'])
plt.xlabel("Ratings")
plt.ylabel("No.of reviews")
plt.title("Ratings vs No.of reviews")
plt.savefig('ratings_chart.png',transparent=True,dpi=50)
plt.show()


# In[10]:


wordcloud=WordCloud(width=800,height=800,background_color='white',min_font_size=10).generate(str(df['review']))


# In[11]:


#plt.figure(figsize=(8,8),facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('review_word.png',transparent=True,dpi=50)
plt.show()


# In[13]:


df=df.drop(['UniqueId','drugName','condition','date','usefulCount'],axis=1)
df2=df2.drop(['UniqueId','drugName','condition','date','usefulCount'],axis=1)


# In[14]:


def prepro(df):
    tokens=word_tokenize(df)
    stemmer=SnowballStemmer('english',ignore_stopwords=True)
    stemmed=[stemmer.stem(word) for word in tokens]
    words=[word for word in stemmed if word.isalpha()]
    stop_words=set(stopwords.words('english'))
    st=[w for w in words if not w in stop_words]
    return st


# In[15]:


df['review']=df['review'].apply(lambda x:prepro(x))
#df2['review']=df2['review'].apply(lambda x:prepro(x))


# In[16]:


def sentiment(df):
  df.loc[df.rating<4,'Sentiment']="Negative"
  df.loc[(df.rating>=4) & (df.rating<7) ,'Sentiment']="Neutral"
  df.loc[(df.rating>=7),'Sentiment']="Positive"
  return df


# In[17]:


df=sentiment(df)


# In[18]:


sns.boxplot(df['rating'],df['Sentiment'])
plt.xlabel("Rating")
plt.ylabel("Sentiment")
plt.title('Box plot')
plt.savefig('boxplot.png',transparent=True,dpi=50)
plt.show()


# In[20]:


pos=df[df['Sentiment']=='Positive'].shape[0]
neg=df[df['Sentiment']=='Negative'].shape[0]
neu=df[df['Sentiment']=='Neutral'].shape[0]
plt.bar(10,pos,3,label='Positive')
plt.bar(15,neg,3,label='Negative')
plt.bar(20,neu,3,label='Neutral')
plt.legend()
plt.ylabel('Number of examples')
plt.title('Proportion of examples')
plt.savefig('barplot.png',transparent=True,dpi=50)
plt.show()


# In[21]:


X=df.drop('Sentiment',axis=1)
y=df['Sentiment']


# In[22]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42,stratify=y)


# In[23]:


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
train_Xv=vectorizer.fit_transform(X_train['review'].astype(str))
test_Xv=vectorizer.transform(X_test['review'].astype(str))


# In[24]:


clf = MLPClassifier(solver='adam', alpha=0.01,activation='relu',hidden_layer_sizes=(150, 75),max_iter=1000,random_state=1,batch_size=27017,learning_rate_init=0.001)


# In[25]:


clf.fit(train_Xv,y_train)


# In[32]:


y_pred=clf.predict(test_Xv)


# In[26]:


clf.score(test_Xv,y_test)


# In[34]:


import pickle

with open('classifier.pkl','wb') as f:
    pickle.dump(clf,f)
with open('vectorizer.pkl','wb') as g:
    pickle.dump(vectorizer,g)


# In[24]:


import pickle
with open('classifier.pkl','rb') as f:
    loaded_clf=pickle.load(f)
with open('vectorizer.pkl','rb') as g:
    loaded_vect=pickle.load(g)


# In[34]:


from sklearn.metrics import confusion_matrix
ConfusionMatrix=confusion_matrix(y_test, y_pred)


# In[36]:


conf=pd.DataFrame(ConfusionMatrix)


# In[37]:


import scikitplot as skplt


# In[56]:


skplt.metrics.plot_confusion_matrix(y_test, y_pred, normalize=True)
plt.savefig('confusion.png',transparent=True,dpi=50)
plt.show()


# In[53]:


Accuracy = format(loaded_clf.score(test_Xv, y_test)*100, '.2f')+ ' %'
file = open('AccuracyPercentage', 'wb')
pickle.dump(Accuracy, file)
file.close()


# In[54]:


with open('AccuracyPercentage','rb') as f:
    loaded_acc=pickle.load(f)

