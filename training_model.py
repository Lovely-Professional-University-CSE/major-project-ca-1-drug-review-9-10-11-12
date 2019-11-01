import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer,PorterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords 

df=pd.read_csv("drugsComTrain_raw.tsv",delimiter='\t')
df2=pd.read_csv("drugsComTest_raw.tsv",delimiter='\t')


df.rename(columns={'Unnamed: 0':'UniqueId'},inplace=True)
df2.rename(columns={'Unnamed: 0':'UniqueId'},inplace=True)

df=df.drop(['UniqueId','drugName','condition','date','usefulCount'],axis=1)
df2=df2.drop(['UniqueId','drugName','condition','date','usefulCount'],axis=1)

def prepro(df):
    tokens=word_tokenize(df)
    stemmer=SnowballStemmer('english',ignore_stopwords=True)
    stemmed=[stemmer.stem(word) for word in tokens]
    words=[word for word in stemmed if word.isalpha()]
    stop_words=set(stopwords.words('english'))
    st=[w for w in words if not w in stop_words]
    return st

df['review']=df['review'].apply(lambda x:prepro(x))
df2['review']=df2['review'].apply(lambda x:prepro(x))

def sentiment(df):
  df.loc[df.rating<4,'Sentiment']="Negative"
  df.loc[(df.rating>=4) & (df.rating<7) ,'Sentiment']="Neutral"
  df.loc[(df.rating>=7),'Sentiment']="Positive"
  return df

df['review']=sentiment(df)

X=df.drop('Sentiment',axis=1)
y=df['Sentiment']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42,stratify=y)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
train_Xv=vectorizer.fit_transform(X_train['review'].astype(str))
test_Xv=vectorizer.transform(X_test['review'].astype(str))

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(solver='adam', alpha=0.01,activation='relu',hidden_layer_sizes=(150, 75),max_iter=1000,random_state=1,batch_size=27017,learning_rate_init=0.001)

clf.fit(train_Xv,y_train)

clf.score(test_Xv,y_test)

from sklearn.metrics import accuracy_score

y_pred=clf.predict(test_Xv)

print(accuracy_score(y_test,y_pred))

import pickle

with open('classifier.pkl','wb') as f:
    pickle.dump(clf,f)
with open('vectorizer.pkl','wb') as g:
    pickle.dump(vectorizer,g)

import pickle
with open('classifier.pkl','rb') as f:
    loaded_clf=pickle.load(f)
with open('vectorizer.pkl','rb') as g:
    loaded_vect=pickle.load(g)

x="Awful medicine, the worst. The side effects outweigh the benefit.  Headache the first night, leg and back pain, Sensitive skin,  just awful. Pain got worse and worse. I changed my meds to ciproflaxcin. I have used this in the past so hopefully, it will continue to help. I even questioned the doc at urgent care to see if I can take cipro and she offered macrobid. Maybe this urgent care and this medication is something they get a deal on....stay away from macrobid."


z=prepro(x)
print(z)

stt=' '.join(map(str,z)) #converting the list to a string
stt=[stt]
vect=loaded_vect.transform(stt)#to make the string iiterableconvert it intoa list
vect.size

y_pred=loaded_clf.predict(vect)



