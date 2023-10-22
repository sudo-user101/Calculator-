import tkinter as k

def press(n):
    global e
    e += str(n)
    if n == ".":
        text_box.insert(k.END, ".")
    else:
       text_box.insert(k.END, str(n) )

def clr():
    global e
    e = text_box.delete(0,k.END)

def delete():
    global e
    text = text_box.get()
    e = text[:-1]
    text_box.delete(0,k.END)
    text_box.insert(k.END,e)

def add(a):
    global e
    e+=a
    text_box.insert(k.END,a)

def minus(mi):
    global e
    e+=mi
    text_box.insert(k.END,mi)
def mutiply(m):
    global e
    e+=m
    text_box.insert(k.END,m)

def di(d):
    global e
    e+=d
    text_box.insert(k.END,d)

def equals():
    global e
    try:
        result = str(eval(e))
        e = result
        text_box.delete(0,k.END)
        text_box.insert(k.END,result)
    except SyntaxError:
        error_Message = "Syntax Error"
        text_box.delete(0,k.END)
        e = text_box.insert(k.END,error_Message)

r = k.Tk()
r.title("Calucaltor")
r.geometry("300x280")
e=""

text_box = k.Entry(r, font=12)
clear = k.Button(r,font=12,text="CLR",command=lambda:clr())
delete_number = k.Button(r,text="Del",font=12,command=lambda:delete())
text_box.grid(row=0,column=0)
clear.grid(row=0,column=1,sticky=k.EW)

frame = k.Frame(r)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=1)
frame.columnconfigure(2,weight=1)
frame.columnconfigure(3,weight=1)
frame.grid()

btn1 = k.Button(frame,text="1",font=12,height=2,width=4,command=lambda:press(1))
btn1.grid(row=0,column=0)
btn2 = k.Button(frame,text="2",font=12,height=2,width=4,command=lambda:press(2))
btn2.grid(row=0,column=1)
btn3 = k.Button(frame,text="3",font=12,height=2,width=4,command=lambda:press(3))
btn3.grid(row=0,column=2)
op1 = k.Button(frame,text="+",font=12,height=2,width=4,command=lambda:add("+"))
op1.grid(row=0,column=3)
btn4 = k.Button(frame,text="4",font=12,height=2,width=4,command=lambda:press(4))
btn4.grid(row=1,column=0)
btn5 = k.Button(frame,text="5",font=12,height=2,width=4,command=lambda:press(5))
btn5.grid(row=1,column=1)
btn6 = k.Button(frame,text="6",font=12,height=2,width=4,command=lambda:press(6))
btn6.grid(row=1,column=2)
op2 = k.Button(frame,text="*",font=12,height=2,width=4,command=lambda:mutiply("*"))
op2.grid(row=1,column=3)
btn7 = k.Button(frame,text="7",font=12,height=2,width=4,command=lambda:press(7))
btn7.grid(row=2,column=0)
btn8 = k.Button(frame,text="8",font=12,height=2,width=4,command=lambda:press(8))
btn8.grid(row=2,column=1)
btn9 = k.Button(frame,text="9",font=12,height=2,width=4,command=lambda:press(9))
btn9.grid(row=2,column=2)
op3 = k.Button(frame,text="/",font=12,height=2,width=4,command=lambda:di("/"))
op3.grid(row=2,column=3)
op4 = k.Button(frame,text=".",font=12,height=2,width=4,command=lambda:press("."))
op4.grid(row=3,column=0)
btn10 = k.Button(frame,text="0",font=12,height=2,width=4,command=lambda:press(0))
btn10.grid(row=3,column=1)
btn11 = k.Button(frame,text="-",font=12,height=2,width=4,command=lambda:minus("-"))
btn11.grid(row=3,column=3)
delete_number = k.Button(frame,text="Del",font=12,height=2,width=4,command=lambda:delete())
delete_number.grid(row=3,column=2)
equal = k.Button(frame, text="=", font=12,height=2,width=4,command=lambda:equals() )
equal.grid(row=4, column=0, columnspan=4, sticky=k.EW)

r.mainloop()