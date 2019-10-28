import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer,PorterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords 
from tkinter import *
import pickle
with open('classifier.pkl','rb') as f:
    loaded_clf=pickle.load(f)
with open('vectorizer.pkl','rb') as g:
    loaded_vect=pickle.load(g)


def prepro(df):
    tokens=word_tokenize(df)
    stemmer=SnowballStemmer('english',ignore_stopwords=True)
    stemmed=[stemmer.stem(word) for word in tokens]
    words=[word for word in stemmed if word.isalpha()]
    stop_words=set(stopwords.words('english'))
    st=[w for w in words if not w in stop_words]
    return st

def vector(x):
  string=' '.join(map(str,x)) 
  string=[string]
  vect=loaded_vect.transform(string)
  return vect


def sentiment():
    mtext=t1.get()
    x=prepro(mtext)
    vect=vector(x)
    pred=loaded_clf.predict(vect)
    entry2=Label(top,text=pred).grid(row=2,column=1)
top=Tk()
t1=StringVar()
name=Label(top,text="Name").grid(row=0,column=0)
e=Entry(top,textvariable=t1).grid(row=0,column=1)
mbutton=Button(top,text='Get Sentiment',command=sentiment).grid(row=1,column=1)
top.mainloop()