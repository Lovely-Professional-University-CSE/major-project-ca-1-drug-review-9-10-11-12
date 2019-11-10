

import pandas as pd
import numpy as np
import os
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
global t1

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
    global t1,root
    print(t1)
    mtext=t1.get()
    x=prepro(mtext)
    vect=vector(x)
    pred=loaded_clf.predict(vect)
    entry2=Label(root,text=pred).pack()

def open_window():
    global t1,root
    top.destroy()
    root= Tk()
    #root.wm_attributes("-fullscreen", "true")
    root.config(bg="black")
    root.title("Predict the Sentiment")
    t1=StringVar()
    canvas1 = Canvas(root, width = 400, height = 300,  relief = 'raised',bg = 'black')
    canvas1.pack()

    label1 =Label(root, text='Predict Or Comment The Sentiment')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

    label2 =Label(root, text='Type Your Review:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label2)
 
    entry1 =Entry (root) 
    canvas1.create_window(200, 140, window=entry1)
    
    B2 = Button(root,text='Get the Sentiment',bg='brown', fg='white', font=('helvetica', 9, 'bold'),command=sentiment)
    canvas1.create_window(200, 180, window=B2)
    print(t1)
    

top=Toplevel()
#top.geometry("600x300+120+120")

top.config(bg ="black")
top.wm_title("ABOUT")
top.wm_attributes("-fullscreen", "true")

take_UI1 = PhotoImage(file ='Input_Image.png')
B1=Button(top, image = take_UI1, cursor="hand2", command = open_window)
B1.pack(anchor=N, padx=500,pady=20,fill='both')
B1.config(width = 150, height = 150)

def Return_H():
	top.destroy()
	os.system('home_page.py')
home_R = PhotoImage(file = 'home.png')
mbutton=Button(top,image=home_R, font=('helv36', 20, 'bold'),fg = 'white',bg='black', cursor="hand2", command = Return_H)
mbutton.pack(anchor=SW, padx =500, pady = 20,fill='both')
mbutton.config(width = 300, height = 120)

def exit_window():
	top.destroy()
    
exit1 = PhotoImage(file = 'Exit_Image.png')
mbutton1=Button(top,image =exit1,command=exit_window)
mbutton1.pack(anchor=SE,padx=500,pady=20,fill='both')
mbutton1.config(width = 300, height = 120)

def Plots():
  top.destroy()
	#os.system('app.py')
  print("do nothing")

bar_plots = PhotoImage(file = 'bar_graph.png')
B2=Button(top,image =bar_plots,text= 'Plots',compound=LEFT,font=('helv36', 60, 'bold'),command=Plots)
B2.pack(anchor=SE,padx=300,pady=20,fill='both')
B2.config(width = 300, height = 300)
"""
def Accuracy():
  top.destroy()
	#os.system('app.py')
  print("do nothing")

accuracy1 = PhotoImage(file = 'features_accuracy.png')
B3=Button(top,image =accuracy1,text= 'Check Accuracy',compound=LEFT,font=('helv36', 60, 'bold'),command=Accuracy)
B3.pack(anchor=SE,padx=10,pady=20,fill='both')
B3.config(width = 100, height = 50)
"""
top.mainloop()