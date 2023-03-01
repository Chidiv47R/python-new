#the calculator endeavour,utiva simple calculator
from tkinter import*
#first import * from tkinter as shown above
##then define the buttons
#first button defines the click function

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

#second button "btnClearDisplay" defines the clear display function of the "C" button on the calculator
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
#the third button defines the funtion of the equal to"=" sign
    
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
#defines the title as calculator
cal = Tk()
cal.title("Calculator")
operator=""
text_Input =StringVar()

#text display on the GUI
#

txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                    bg="powder blue", justify='right').grid(columnspan=4)

#the calculator is 4X4 number and symbol interface that would return sum, substration and divsion of values entered
#===the following 4 rows defines button 7,8,9,and +, and also gives the buttons dimension font colour and position on the 4x4 display

btn7=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="7",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="8",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="9",command=lambda:btnClick(9)).grid(row=1,column=2)

Addition=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="+",command=lambda:btnClick("+")).grid(row=1,column=3)

#============================================================== row one above
#===the following 4 rows defines button 4,5,6,and -, and also gives the buttons dimension font colour and position on the 4x4 display row 2

btn4=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="4",command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="5",command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="6",command=lambda:btnClick(6)).grid(row=2,column=2)

Subtration=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="-",command=lambda:btnClick("-")).grid(row=2,column=3)

#============================================================================= row two above
#===the following 4 rows defines button 1,2,3,and *, and also gives the buttons dimension font colour and position on the 4x4 display row 3

btn1=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="1",command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="2",command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="3",command=lambda:btnClick(3)).grid(row=3,column=2)

Multiplication=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'), text="*",command=lambda:btnClick("*")).grid(row=3,column=3)

#============================================================================================= row three above
#===the following 4 rows defines button 0,C,=,and /, and also gives the buttons dimension font colour and position on the 4x4 display row 4
    
btn0=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'), text="0",command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'), text="C",command=btnClearDisplay).grid(row=4,column=1)

btnEquals=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'), text="=",command=btnEqualsInput).grid(row=4,column=2)

Division=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'), text="/",command=lambda:btnClick("/")).grid(row=4,column=3)
    
#=================================================================================row four above final calculator line





    
cal.mainloop()
