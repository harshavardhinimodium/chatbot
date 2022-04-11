from tkinter import *
import random as r
from tkinter import messagebox
tk=Tk()
tk.configure(background="magenta")

def send():
    send="You : "+e.get()
    txt.insert(END,"\n"+send)

    if(e.get()=="hi"):
        txt.insert(END,"\n"+"Bot : Hello!! ")
    elif(e.get()==("how are you?" )):
        txt.insert(END,"\n"+"Bot : I am fine . How do you do")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"what made you chat with me")
    elif(e.get()=="i am upset"):
        txt.insert(END,"\n"+"Bot : I think I can help . Please! Click the Jokes button ")
    elif (e.get()=="who made you"):
        txt.insert(END,"\n sorry I can't tell you it's a top secret")
    elif e.get() == "not so funny":
        txt.insert(END, "\n" + "Sorry try some more jokes")
    elif e.get() == "i liked it":
        txt.insert(END, "\n" + " Thank you")

    else:
        txt.insert(END,"\n Sorry! I didn't get you")
    e.delete(0,END)


def joke(x):
    if (x==2):
        txt.insert(END,"\n"+"Bot :Newest entry: A Japanese student: Master Aykodo, why do Europeans think we look all the same? \n          The master replied : I'm not master Aykodo. ")
    elif x==1:
        txt.insert(END,"\n"+"Bot : The best first: What to call a bear who’s lost all its teeth? --> A guzmmy bear!")
    elif x==3:
        txt.insert(END, "\n" +"Recently added: Why do they actually prefer non-swimmers in the Navy? They defend their ship with a lot more enthusiasm")
    elif x==4:
        txt.insert(END, "\n" + "Baby: This potato salad makes me sad. \n mom: Why?\nBaby: All these potatoes could have been fries!")


def jokes():
    jks=[1,2,3,4]
    x=r.choice(jks)
    joke(x)

def exit():
    bye=messagebox.askyesno("Quit","Do you wanna leave..?")
    if bye==True:
        tk.quit()



txt=Text(tk)
txt.grid(row=0,column=0,columnspan=2)
txt.insert(END,"\nBot : please use lower case letters for conversation with me")
e=Entry(tk,width=100)
send=Button(tk,text="SEND",command=send).grid(row=1,column=1)
jokes=Button(tk,text="Jokes",command=jokes).grid(row=2,column=1)
bye=Button(tk,text="Quit",command=exit).grid(row=0,column=1)
e.grid(row=1,column=0)
tk.title("Mini Chatter")
tk.mainloop()
