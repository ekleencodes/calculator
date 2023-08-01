from tkinter import*
import math
root=Tk()
root.title("Calculator")
root.minsize(400,400)
root.resizable(0,0)
inputScreen=Entry(root,borderwidth=5,width=35)
inputScreen.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def click(number):
    inputScreen.insert(END,number)
def clear():
    inputScreen.delete(0,END)
def add():
    num1=inputScreen.get()
    global firstNumber
    global math
    math="addition"
    firstNumber=int(num1)
    inputScreen.delete(0,END)
def equals():
    num2=inputScreen.get()
    inputScreen.delete(0,END)
    if math =="addition":
        inputScreen.insert(0,int(num2)+int(firstNumber))
    if math =="multiplication":
        inputScreen.insert(0,int(num2)*int(firstNumber))
    if math =="division":
        inputScreen.insert(0,int(firstNumber)/int(num2))
    if math =="subtraction":
        inputScreen.insert(0,int(firstNumber)-int(num2))
def multiply():  
    num1=inputScreen.get()
    global firstNumber
    global math
    math="multiplication"  
    firstNumber=int(num1)
    inputScreen.delete(0,END)
def division():
      num1=inputScreen.get()
      global firstNumber
      global math
      math="division"  
      firstNumber=int(num1)
      inputScreen.delete(0,END)
def subtract():
    num1=inputScreen.get()
    global firstNumber
    global math
    math="subtraction"  
    firstNumber=int(num1)
    inputScreen.delete(0,END)
btn1=Button(root,text="1",padx=40,pady=20,command=lambda: click(1))
btn2=Button(root,text="2",padx=40,pady=20,command=lambda: click(2))
btn3=Button(root,text="3",padx=40,pady=20,command=lambda: click(3))
btn4=Button(root,text="4",padx=40,pady=20,command=lambda: click(4))
btn5=Button(root,text="5",padx=40,pady=20,command=lambda: click(5))
btn6=Button(root,text="6",padx=40,pady=20,command=lambda: click(6))
btn7=Button(root,text="7",padx=40,pady=20,command=lambda: click(7))
btn8=Button(root,text="8",padx=40,pady=20,command=lambda: click(8))
btn9=Button(root,text="9",padx=40,pady=20,command=lambda: click(9))
btn0=Button(root,text="0",padx=40,pady=20,command=lambda: click(0))

btnAdd=Button(root,text="+",padx=40,pady=20,command=add)
btnEquals=Button(root,text="=",padx=90,pady=20,command=equals)
btnClear=Button(root,text="clear",padx=80,pady=20,command=clear)
btnMultiply=Button(root,text="*",padx=42,pady=20,command=multiply)
btnDivide=Button(root,text="/",padx=40,pady=20,command=division)
btnSubtract=Button(root,text="-",padx=42,pady=20,command=subtract)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btn0.grid(row=4,column=0)
btnAdd.grid(row=5,column=0)
btnEquals.grid(row=5,column=1,columnspan=2)
btnClear.grid(row=4,column=1,columnspan=2)
btnSubtract.grid(row=6,column=0)
btnMultiply.grid(row=6,column=1)
btnDivide.grid(row=6,column=2)


root.mainloop()