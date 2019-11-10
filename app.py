from preprocess import *
from tkinter import *
def sentiment():
    global t1,root
    print(t1)
    mtext=t1.get()
    x=prepro(mtext)
    vect=vector(x)
    pred=loaded_clf.predict(vect)
    entry2=Label(root,text=pred)
    entry2.pack()
    
def open_window():
    global t1,root
    #top.destroy()
    root = Tk()
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