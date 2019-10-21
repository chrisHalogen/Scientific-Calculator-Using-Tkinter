from tkinter import *
import math
import parser
import tkinter.messagebox

win = Tk()
win.title("Scientific Calculator")
win.configure(background = "white")
win.resizable(width = False,height = False)
win.geometry("343x530+0+0")

calc = Frame(win)
calc.configure(background = "white")
calc.grid()

defText= "0"
txtmain= Label(calc, width = 14, text = defText, bd=5, font= ("arial",30,"bold"), bg = "green",fg="black", anchor = E)
txtmain.grid(row=0,column=0,columnspan=4, pady=1)

txtlabel = Label(calc, font= ("arial",30,"bold"), bg = "white", text = "Scientific Mode", justify = RIGHT)
txtlabel.grid(row=0, column=4, columnspan =4, pady=1)

#=========================Button Commands==================================#
def cmd9():
        txt = txtmain.cget("text")
        if txt == "0":
                txtmain.configure(text= "9")
        else:
                text1 = txtmain.cget("text") + "9"
                txtmain.configure(text= text1)
def cmd8():
        txt = txtmain.cget("text")
        if txt == "0":
                txtmain.configure(text= "8")
        else:
                text1 = txtmain.cget("text") + "8"
                txtmain.configure(text= text1)
def cmd7():
        txt = txtmain.cget("text")
        if txt == "0":
                txtmain.configure(text= "7")
        else:
                text1 = txtmain.cget("text") + "7"
                txtmain.configure(text= text1)
def cmd6():
        txt = txtmain.cget("text")
        if txt == "0":
                txtmain.configure(text= "6")
        else:
                text1 = txtmain.cget("text") + "6"
                txtmain.configure(text= text1)
def cmd5():
        txt = txtmain.cget("text")
        if txt == "0":
                txtmain.configure(text= "5")
        else:
                text1 = txtmain.cget("text") + "5"
                txtmain.configure(text= text1)
def cmd4():
        txt = txtmain.cget("text")
        if txt == "0":
                txtmain.configure(text= "4")
        else:
                text1 = txtmain.cget("text") + "4"
                txtmain.configure(text= text1)
def cmd3():
        txt = txtmain.cget("text")
        if txt == "0":
                txtmain.configure(text= "3")
        else:
                text1 = txtmain.cget("text") + "3"
                txtmain.configure(text= text1)
def cmd2():
        txt = txtmain.cget("text")
        if txt == "0":
                txtmain.configure(text= "2")
        else:
                text1 = txtmain.cget("text") + "2"
                txtmain.configure(text= text1)
def cmd1():
        txt = txtmain.cget("text")
        if txt == "0":
                txtmain.configure(text= "1")
        else:
                text1 = txtmain.cget("text") + "1"
                txtmain.configure(text= text1)
def cmd0():
        txt = txtmain.cget("text")
        if txt != "0":
                text1 = txtmain.cget("text") + "0"
                txtmain.configure(text= text1)
def cmdDot():
        isDot = False
        txt = txtmain.cget("text")
        for i in txt:
                if i == ".":
                        isDot = True
        if isDot == False:
                text1 = txtmain.cget("text") + "."
                txtmain.configure(text= text1)

#============================End of Button Commands===================================


#============================Standard Calculator Commands=============================

class Calculate:
        def __init__(self,num1,num2,op):
                self.num1=num1
                self.num2=num2
                self.op = op
        def setNum1(self,x):
                self.num1 = x
        def setNum2(self,x):
                self.num2 = x
        def setOp(self,x):
                self.op = x
        def calculate(self):
                if self.op == "+":
                        result = self.num1 + self.num2
                elif self.op == "-":
                        result = self.num1 - self.num2
                elif self.op == "*":
                        result = self.num1 * self.num2
                elif self.op == "/":
                        if self.num2 == 0:
                                txtmain.configure(text= "ERROR!!!")
                        else:
                                result = self.num1 / self.num2
                elif self.op == "mod":
                        result = self.num1 % self.num2
                else:
                        result = 0
                return result
operation = Calculate(0,0,"+")  

def cmdPlus():
        num1 = eval(txtmain.cget("text"))
        op = "+"
        txtmain.configure(text= "0")
        operation.setNum1(num1)
        operation.setOp(op)

def cmdMinus():
        num1 = eval(txtmain.cget("text"))
        op = "-"
        txtmain.configure(text= "0")
        operation.setNum1(num1)
        operation.setOp(op)
def cmdTimes():
        num1 = eval(txtmain.cget("text"))
        op = "*"
        txtmain.configure(text= "0")
        operation.setNum1(num1)
        operation.setOp(op)
def cmdDiv():
        num1 = eval(txtmain.cget("text"))
        op = "/"
        txtmain.configure(text= "0")
        operation.setNum1(num1)
        operation.setOp(op)
def cmdSqrt():
        txt = eval(txtmain.cget("text"))
        txt = math.sqrt(txt)
        txtmain.configure(text= txt)
def cmdMod():
        num1 = eval(txtmain.cget("text"))
        op = "mod"
        txtmain.configure(text= "0")
        operation.setNum1(num1)
        operation.setOp(op)

def cmdClearAll():
        txtmain.configure(text= "0")
def cmdClear():
        alpha= txtmain.cget("text")
        newalpha = ""
        m = len(alpha)
        if m==1:
               txtmain.configure(text= "0") 
        else:
                x = m - 1
                for i in range(x):
                        newalpha += alpha[i]
                txtmain.configure(text= newalpha)
        
def btnEquals():
        num2 = eval(txtmain.cget("text"))
        operation.setNum2(num2)
        result = operation.calculate()
        
        result = str(result)
        txtmain.configure(text= result)

#===========================End of Standard Calculator Commands=====================

#===========================Scientific Calculator commands==========================

def cmdPi():
        num1 = math.pi
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdSin():
        num1 = eval(txtmain.cget("text"))
        num1 = math.sin(math.radians(num1))
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdCos():
        num1 = eval(txtmain.cget("text"))
        num1 = math.cos(math.radians(num1))
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdTan():
        num1 = eval(txtmain.cget("text"))
        num1 = math.tan(math.radians(num1))
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdTau():
        num1 = eval(txtmain.cget("text"))
        num1 = math.tau
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdSinh():
        num1 = eval(txtmain.cget("text"))
        num1 = math.sinh(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdCosh():
        num1 = eval(txtmain.cget("text"))
        num1 = math.cosh(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdTanh():
        num1 = eval(txtmain.cget("text"))
        num1 = math.tanh(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdLog():
        num1 = eval(txtmain.cget("text"))
        num1 = math.log(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdExp():
        num1 = eval(txtmain.cget("text"))
        num1 = math.exp(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdE():
        num1 = eval(txtmain.cget("text"))
        num1 = math.e
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdaSin():
        num1 = eval(txtmain.cget("text"))
        num1 = math.asin(math.radians(num1))
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdaCos():
        num1 = eval(txtmain.cget("text"))
        num1 = math.acos(math.radians(num1))
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdaTan():
        num1 = eval(txtmain.cget("text"))
        num1 = math.atan(math.radians(num1))
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdLog2():
        num1 = eval(txtmain.cget("text"))
        num1 = math.log2(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdPlusMinus():
        num1 = eval(txtmain.cget("text"))
        if num1 < 0:
                num1 = num1 * (-1)
        elif num1 == 0:
                num1 = num1
        else:
                num1 = -num1
        txtmain.configure(text= num1)
def cmdLog10():
        num1 = eval(txtmain.cget("text"))
        num1 = math.log10(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdaSinh():
        num1 = eval(txtmain.cget("text"))
        num1 = math.asinh(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdaCosh():
        num1 = eval(txtmain.cget("text"))
        num1 = math.acosh(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)
def cmdaTanh():
        num1 = eval(txtmain.cget("text"))
        num1 = math.atanh(num1)
        num1 = round(num1,6)
        txtmain.configure(text= num1)

#============================End of Scientific Calculator Commands=============== 

#============================ Standard Calculator Controls =================================    

btn9 = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "9",bd=4, command = cmd9)
btn9.grid(row=2,column=2,pady=1)
btn8 = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "8", bd=4, command = cmd8)
btn8.grid(row=2,column=1,pady=1)
btn7 = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "7", bd=4, command = cmd7)
btn7.grid(row=2,column=0,pady=1)
btn6 = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "6", bd=4, command = cmd6)
btn6.grid(row=3,column=2,pady=1)
btn5 = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "5", bd=4, command = cmd5)
btn5.grid(row=3,column=1,pady=1)
btn4 = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "4", bd=4, command = cmd4)
btn4.grid(row=3,column=0,pady=1)
btn3 = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "3", bd=4, command = cmd3)
btn3.grid(row=4,column=2,pady=1)
btn2 = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "2", bd=4, command = cmd2)
btn2.grid(row=4,column=1,pady=1)
btn1 = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "1", bd=4, command = cmd1)
btn1.grid(row=4,column=0,pady=1)


btnClear = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "C", bd=4, command = cmdClear)
btnClear.grid(row=1,column=0,pady=1)
btnClearAll = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "CE", bd=4,command=cmdClearAll)
btnClearAll.grid(row=1,column=1,pady=1)
btnSqrt = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "√", bd=4,command = cmdSqrt)
btnSqrt.grid(row=1,column=2,pady=1)
btnPlus = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "+", bd=4, command=cmdPlus)
btnPlus.grid(row=1,column=3,pady=1)
btnMinus = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "-", bd=4,command=cmdMinus)
btnMinus.grid(row=2,column=3,pady=1)
btnTimes = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "*", bd=4,command=cmdTimes)
btnTimes.grid(row=3,column=3,pady=1)
btnDiv = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "/", bd=4,command=cmdDiv)
btnDiv.grid(row=4,column=3,pady=1)

btnZero = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "0", bd=4, command = cmd0)
btnZero.grid(row=5,column=1,pady=1)
btnDot = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= ".", bd=4, command = cmdDot)
btnDot.grid(row=5,column=0,pady=1)
btnPlusMinus = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= chr(177), bd=4, command = cmdPlusMinus)
btnPlusMinus.grid(row=5,column=2,pady=1)
btnEquals = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "=", bd=4, command = btnEquals)
btnEquals.grid(row=5,column=3,pady=1)
#==========================End of Standard Calculator Controls==============================

#===============================Scientific Calculator controls==========================================

btnPi = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "ﬨ", bd=4, command = cmdPi)
btnPi.grid(row=1,column=4,pady=1)
btnSin = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "Sin", bd=4, command = cmdSin)
btnSin.grid(row=1,column=5,pady=1)
btnCos = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "Cos", bd=4, command = cmdCos)
btnCos.grid(row=1,column=6,pady=1)
btnTan = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "Tan", bd=4, command = cmdTan)
btnTan.grid(row=1,column=7,pady=1)

btn2Pi = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "Tau", bd=4, command = cmdTau)
btn2Pi.grid(row=2,column=4,pady=1)
btnSinh = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "Sinh", bd=4, command = cmdSinh)
btnSinh.grid(row=2,column=5,pady=1)
btnCosh = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "Cosh", bd=4, command = cmdCosh)
btnCosh.grid(row=2,column=6,pady=1)
btnTanh = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "Tanh", bd=4, command = cmdTanh)
btnTanh.grid(row=2,column=7,pady=1)

btnLog = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "LogE", bd=4, command = cmdLog)
btnLog.grid(row=3,column=4,pady=1)
btnExp = Button(calc,  width = 4, height = 2, font=("arial",20,"bold"), text= "Exp", bd=4, command = cmdExp)
btnExp.grid(row=3,column=5,pady=1)
btnMod = Button(calc,  width = 4, height = 2, font=("arial",20,"bold"), text= "Mod", bd=4, command = cmdMod)
btnMod.grid(row=3,column=6,pady=1)
btnE = Button(calc,  width = 4, height = 2, font=("arial",20,"bold"), text= "e", bd=4, command = cmdE)
btnE.grid(row=3,column=7,pady=1)

btnLog2 = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "Log2", bd=4, command = cmdLog2)
btnLog2.grid(row=4,column=4,pady=1)
btnaSin = Button(calc,  width = 4, height = 2, font=("arial",20,"bold"), text= "aSin", bd=4, command = cmdaSin)
btnaSin.grid(row=4,column=5,pady=1)
btnaCos = Button(calc,  width = 4, height = 2, font=("arial",20,"bold"), text= "aCos", bd=4, command = cmdaCos)
btnaCos.grid(row=4,column=6,pady=1)
btnaTan = Button(calc, width = 4, height = 2, font=("arial",20,"bold"), text= "aTan", bd=4, command = cmdaTan)
btnaTan.grid(row=4,column=7,pady=1)

btnLog10 = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "Log10", bd=4, command = cmdLog10)
btnLog10.grid(row=5,column=4,pady=1)
btnaSinh = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "aSinh", bd=4, command = cmdaSinh)
btnaSinh.grid(row=5,column=5,pady=1)
btnaCosh = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "aCosh", bd=4, command = cmdaCosh)
btnaCosh.grid(row=5,column=6,pady=1)
btnaTanh = Button(calc, bg="green", width = 4, height = 2, font=("arial",20,"bold"), text= "aTanh", bd=4, command = cmdaTanh)
btnaTanh.grid(row=5,column=7,pady=1)

#=================================End of Scientific Calculator Controls=========================================


#==============================================Menu Area========================================================

def cmdExit():
    msg = tkinter.messagebox.askyesno("The Halogenic Calculator", "Confirm if you want to Exit")
    if msg > 0 :
        win.destroy()
def cmdStandard():
    win.resizable(width = False,height = False)
    win.geometry("343x530+0+0")
def cmdScientific():
    win.resizable(width = False,height = False)
    win.geometry("670x530+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Standard", command = cmdStandard)
filemenu.add_command(label = "Scientific", command = cmdScientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = cmdExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu = helpmenu)
helpmenu.add_command(label="Help")

win.config(menu=menubar)

#===========================End of Menu Area=========================================

win.mainloop()