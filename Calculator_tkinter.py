import tkinter as tk

#creating tkinter window and making the window fixed sized
cal = tk.Tk()
cal.title('Basic Calculator')
cal.resizable(False, False)

#continuously update input with clicks
def click(Number):
    global operator
    operator = operator + str(Number)
    variable.set(operator)

#clear input field
def clear():
    global operator
    operator = ''
    variable.set(operator)

#evaluate the expression
def sum():
    global operator
    operator = str(eval(operator))
    variable.set(operator)

operator=''

#create an instance of the input
variable = tk.StringVar()
display = tk.Entry(cal, font=('arial', 20, 'bold'), bd=25, textvariable=variable, justify='right')
display.grid(columnspan=5)

#first row
buttonleft = tk.Button(cal, text='(', font = ('arial', 20, 'bold'), bd=5, padx=13, command = lambda : click('('))
buttonleft.grid(row=1, column=0)

buttonright = tk.Button(cal, text=')', font = ('arial', 20, 'bold'), bd=5, padx=13, command = lambda : click(')'))
buttonright.grid(row=1, column=1)

buttonperc = tk.Button(cal, text='%', font = ('arial', 20, 'bold'), bd=5, padx=6, command = lambda : click('/100'))
buttonperc.grid(row=1, column=2)

buttonplus = tk.Button(cal, text='+', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click('+'))
buttonplus.grid(row=1, column=4)

#second row
button7 = tk.Button(cal, text='7', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(7))
button7.grid(row=2, column=0)

button8 = tk.Button(cal, text='8', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(8))
button8.grid(row=2, column=1)

button9 = tk.Button(cal, text='9', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(9))
button9.grid(row=2, column=2)

buttonminus = tk.Button(cal, text='-', font = ('arial', 20, 'bold'), bd=5, padx=13, command = lambda : click('-'))
buttonminus.grid(row=2, column=4)

#third row
button4 = tk.Button(cal, text='4', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(4))
button4.grid(row=3, column=0)

button5 = tk.Button(cal, text='5', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(5))
button5.grid(row=3, column=1)

button6 = tk.Button(cal, text='6', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(6))
button6.grid(row=3, column=2)

buttonmulti = tk.Button(cal, text='x', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click('*'))
buttonmulti.grid(row=3, column=4)

#fourth row
button1 = tk.Button(cal, text='1', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(1))
button1.grid(row=4, column=0)

button2 = tk.Button(cal, text='2', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(2))
button2.grid(row=4, column=1)

button3 = tk.Button(cal, text='3', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(3))
button3.grid(row=4, column=2)

buttondiv = tk.Button(cal, text='/', font = ('arial', 20, 'bold'), bd=5, padx=14, command = lambda : click('/'))
buttondiv.grid(row=4, column=4)

#fifth row
button0 = tk.Button(cal, text='0', font = ('arial', 20, 'bold'), bd=5, padx=10, command = lambda : click(0))
button0.grid(row=5, column=0)

buttonpoint = tk.Button(cal, text='.', font = ('arial', 20, 'bold'), bd=5, padx=15, command = lambda : click('.'))
buttonpoint.grid(row=5, column=1)

buttonclear = tk.Button(cal, text='C', font = ('arial', 20, 'bold'), bd=5, padx=9, command = clear)
buttonclear.grid(row=5, column=2)

buttonequal = tk.Button(cal, text='=', font = ('arial', 20, 'bold'), bd=5, padx=10, command = sum)
buttonequal.grid(row=5, column=4)

#infinite or event based loop creation
cal.mainloop()