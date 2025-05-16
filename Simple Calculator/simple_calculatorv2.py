from tkinter import *
# HOW THE CODE WORKS
#This code works based in the global variables f_num, sign_fix, mult_or_sum 1 and 2. And mult_or_div
#A substraction its a sum of a positive number with a negative number, so the indirectly the subtraction is a sum. Therefore the mult_or_sum 1 and 2 are responsibles for
#changing the operation for summing or multiplying(a division is an inverse multiplication so its kind of a multiplication either)
#The mult_or_sum 1 can just be 0 or 1 as well the mult_or_sum_2
#When mult_or_sum1 = 1, and mult_or_sum2 = 0, u have a multiplication, the oposite u will get and sum
#the sign_fix will change the sign of the sum to recognize if it is a subtraction or not
#The calculator already shows a previous result in the top of the screen before clicking on the equal button. And when u click in the equal button you have the resulted printed
#in the right end of the screen, this is why I used 3 Entrys for the screen.

#PROBLEMS:
#I didnt notice any problem that affects the working of it. But the code is kind a mess yet. I used a lot of def's and global variable and in the future i wanna use classes
#and reduce the quantity of functions but without changing the logic of the global variable. Beyond this I intend to separate the code in differents files in sake of organizing it. 

root = Tk()
global f_num
f_num = 0

global f_ans
f_ans=0

global sign_fix
sign_fix = 1

global mult_or_sum_1
mult_or_sum_1 = 0

global mult_or_sum_2
mult_or_sum_2 = 1

global mult_or_div
mult_or_div = 1

def call_ans():
    global f_ans

    display.delete(0,END)
    result_display.delete(0,END)
    display.delete(0,END)

    display.insert(0, f_ans)

def insert_number(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current)+str(number))
def clear_fc():
    global sign_fix
    global mult_or_sum_1
    mult_or_sum_1 = 0
    global mult_or_sum_2
    mult_or_sum_2 = 1
    global mult_or_div
    mult_or_div = 1
    sign_fix=1
    display.delete(0,END)
    past_display.delete(0, END)
    result_display.delete(0,END)
    global f_num
    f_num = 0
def add_operation():
    result_display.delete(0,END)
    first_number = display.get()
    global mult_or_sum_2
    global mult_or_sum_1
    global mult_or_div
    global sign_fix
    global f_num
    global mult_or_div
    if not first_number:
        f_num = f_num + 0
    else:
        first_number = float(first_number)
        f_num = f_num*mult_or_sum_1*(first_number**mult_or_div) + mult_or_sum_2*(f_num + sign_fix*(int(first_number)))
    sign_fix = 1
    mult_or_sum_1 = 0
    mult_or_sum_2 = 1
    display.delete(0, END)
    past_display.delete(0, END)
    past_display.insert(0,str(f_num))
def minus_operation():
    result_display.delete(0,END)
    first_number = display.get()
    global f_num
    global sign_fix
    global mult_or_sum_1
    global mult_or_sum_2
    global mult_or_div

    if not first_number:
        f_num = f_num + 0
    else:
        first_number = float(first_number)
        f_num = f_num*mult_or_sum_1*(first_number**mult_or_div) + mult_or_sum_2*(f_num + sign_fix*(int(first_number)))
    sign_fix = -1
    mult_or_sum_1 = 0
    mult_or_sum_2 = 1
    display.delete(0, END)
    past_display.delete(0, END)
    past_display.insert(0,str(f_num))

def mult_operation():
    result_display.delete(0,END)
    first_number = display.get()
    global f_num
    global sign_fix
    global mult_or_sum_1
    global mult_or_sum_2
    global mult_or_div

    if not first_number:
        f_num = f_num + 0
    else:
        first_number = float(first_number)
        f_num = f_num*mult_or_sum_1*(first_number**mult_or_div) + mult_or_sum_2*(f_num + sign_fix*(int(first_number)))
    sign_fix = -1
    mult_or_div = 1
    mult_or_sum_1 = 1
    mult_or_sum_2 = 0
    display.delete(0, END)
    past_display.delete(0, END)
    past_display.insert(0,str(f_num))

def div_operation():
    result_display.delete(0,END)
    first_number = display.get()
    global f_num
    global sign_fix
    global mult_or_sum_1
    global mult_or_sum_2
    global mult_or_div

    if not first_number:
        f_num = f_num + 0
    else:
        first_number = float(first_number)
        f_num = f_num*mult_or_sum_1*(first_number**mult_or_div) + mult_or_sum_2*(f_num + sign_fix*(int(first_number)))
    sign_fix = -1
    mult_or_div = -1
    mult_or_sum_1 = 1
    mult_or_sum_2 = 0
    display.delete(0, END)
    past_display.delete(0, END)
    past_display.insert(0,str(f_num))

def outcoming_fc():
    global f_num
    global f_ans
    global sign_fix
    global mult_or_sum_2
    global mult_or_sum_1
    global mult_or_div
    if not display.get():
        displaynow = 0
    else:
        displaynow = float(display.get())
    past_display.delete(0, END)
    display.delete(0,END)
    result_display.delete(0,END)
    f_num = f_num*mult_or_sum_1*(displaynow**mult_or_div) + mult_or_sum_2*(f_num + sign_fix*displaynow)
    result_display.insert(0, f_num)
    f_ans = f_num
root.title("Simple Calculator - V2")
root.configure(bg="white")

past_display = Entry(root, borderwidth=0, width= 20, font=("Arial",12), fg="gray")
past_display.grid(row=0, column=0, columnspan=3, ipady=5, ipadx=5, rowspan=1)

button_ans = Button(root, text="Ans", padx=15, pady=5, borderwidth=0,highlightthickness=0, command=call_ans)
button_ans.grid(column=3, row=0, columnspan=5)

display = Entry(root, borderwidth=0, width=25, font=("Arial",11), fg="black")
display.grid(row=1, column=0, columnspan=3, ipady=5, ipadx=5, rowspan=1)

result_display = Entry(root, borderwidth=0, width=8, font=("Arial",16), fg="green")
result_display.grid(row=1, column=3, columnspan=5, ipady=5, ipadx=0, rowspan=1)



button_1 = Button(root, text="1", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(1))
button_2 = Button(root, text="2", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(2))
button_3 = Button(root, text="3", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(3))

button_4 = Button(root, text="4", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(4))
button_5 = Button(root, text="5", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(5))
button_6 = Button(root, text="6", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(6))

button_7 = Button(root, text="7", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(7))
button_8 = Button(root, text="8", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(8))
button_9 = Button(root, text="9", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(9))

button_0 = Button(root, text="0", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: insert_number(0))

button_add = Button(root, text="+", padx=38,pady=20, borderwidth=0,highlightthickness=0, command=lambda: add_operation())
button_less = Button(root, text="-", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: minus_operation())
button_multiply = Button(root, text="X", padx=39,pady=20, borderwidth=0,highlightthickness=0, command=lambda: mult_operation())
button_divide = Button(root, text="/", padx=40,pady=20, borderwidth=0,highlightthickness=0, command=lambda: div_operation())

button_equal = Button(root, text="=", borderwidth=0,highlightthickness=0, padx=39,pady=20, command=lambda: outcoming_fc())
button_clear = Button(root, text="Clear", borderwidth=0,highlightthickness=0, padx=30,pady=20, command=lambda: clear_fc())

#put the buttons on the screen 
button_1.grid(column=0, row=4)
button_2.grid(column=1, row=4)
button_3.grid(column=2, row=4)

button_4.grid(column=0, row=3)
button_5.grid(column=1, row=3)
button_6.grid(column=2, row=3)

button_7.grid(column=0, row=2)
button_8.grid(column=1, row=2)
button_9.grid(column=2, row=2)

button_0.grid(column=0, row=5, columnspan=1)

button_add.grid(column=3,row=2, columnspan=10)
button_equal.grid(column=2,row=5, columnspan=1, rowspan=1)
button_clear.grid(column=0,row=5, columnspan=3)
button_less.grid(column=3,row=3, columnspan=10)
button_multiply.grid(column=3,row=4, columnspan=10)
button_divide.grid(column=3,row=5, columnspan=10)


root.mainloop()
