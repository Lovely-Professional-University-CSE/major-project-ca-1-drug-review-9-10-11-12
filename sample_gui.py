from preprocess import *
from tkinter import * 
def sentiment():
    mtext=t1.get()
    x=prepro(mtext)
    vect=vector(x)
    pred=loaded_clf.predict(vect)
    entry2=Label(top,text=pred[0]).grid(row=2,column=1)
top=Tk()
t1=StringVar()
name=Label(top,text="Name").grid(row=0,column=0)
e=Entry(top,textvariable=t1).grid(row=0,column=1)
mbutton=Button(top,text='Get Sentiment',command=sentiment).grid(row=1,column=1)
top.mainloop()
