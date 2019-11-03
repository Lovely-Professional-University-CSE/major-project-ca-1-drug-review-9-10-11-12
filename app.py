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
nltk.download('punkt')
nltk.download('stopwords')
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
def open_window():
    root = Toplevel()
    root.geometry("600x300+120+120")
    root.title("Predict the Sentiment")
    root.config(bg="cyan")
    t1=StringVar()
    name=Label(root,text="Name")
    name.place(x=200,y=100)
    e=Entry(root,textvariable=t1)
    e.place(x=238,y=100)
    button1 = Button(root, text = "Get Sentiment",command = sentiment)
    button1.place(x=245,y=120)    
top=Tk()
top.geometry("600x300+120+120")
top.config(bg ="blue")
top.title("Top Window")
mbutton=Button(top,text='Enter review of your choise',command=open_window)
mbutton.pack()
top.mainloop()
