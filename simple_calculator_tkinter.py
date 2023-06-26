import tkinter as tk

root=tk.Tk()
root.title("calculator")
root.geometry("400x388") 
root.minsize(400,388)
root.maxsize(400,388)
root.configure(background="black")
root.iconbitmap(r'cal.ico') 
def button_click(number):
    current=eny.get()
    eny.delete(0,"end")
    eny.insert(0,str(current)+str(number))
def clear():
    eny.delete(0,"end")
def button_add():
    first_number=eny.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    eny.delete(0,"end")
def button_sub():
    first_number=eny.get()
    global f_num
    global math
    math="subtract"
    f_num=int(first_number)
    eny.delete(0,"end")
def button_mul():
    first_number=eny.get()
    global f_num
    global math
    math="mul"
    f_num=int(first_number)
    eny.delete(0,"end")
def button_div():
    first_number=eny.get()
    global f_num
    global math
    math="div"
    f_num=int(first_number)
    eny.delete(0,"end")
def button_equal():
    second_number=eny.get()
    eny.delete(0,"end")
    if math=="addition":
        eny.insert(0,f_num+int(second_number))
    if math=="subtract":
        eny.insert(0,f_num - int(second_number))
    if math=="mul":
        eny.insert(0,f_num*int(second_number))
    if math=="div":
        eny.insert(0,f_num/int(second_number))





eny=tk.Entry(root,fg="white",bg="black",width=59,borderwidth=21)
eny.grid(rowspan=4,columnspan=4)
nine=tk.Button(root,text="9",relief="sunken",width=10,height=3,fg="black",bg="grey",font=('Arial', 12),command=lambda:button_click(9))
nine.grid(row=4,column=0,sticky="w",pady=8) 
eight=tk.Button(root,text="8",relief="sunken",width=10,height=3,fg="black",bg="grey",font=12,command=lambda:button_click(8))
eight.grid(row=4,column=1,sticky="w",pady=8)
seven=tk.Button(root,text="7",relief="sunken",width=10,height=3,fg="black",bg="grey",font=12,command=lambda:button_click(7))
seven.grid(row=4,column=2,sticky="w",pady=8)

six=tk.Button(root,text="6",width=10,relief="sunken",height=3,fg="black",bg="grey",font=12,command=lambda:button_click(6)) 
six.grid(row=5,column=0,sticky="w",pady=8)
five=tk.Button(root,text="5",relief="sunken",width=10,height=3,fg="black",bg="grey",font=12,command=lambda:button_click(5))
five.grid(row=5,column=1,sticky="w",pady=8)
four=tk.Button(root,text="4",relief="sunken",width=10,height=3,fg="black",bg="grey",font=12,command=lambda:button_click(4))
four.grid(row=5,column=2,sticky="w",pady=8)
three=tk.Button(root,text="3",relief="sunken",width=10,height=3,fg="black",bg="grey",font=12,command=lambda:button_click(3))
three.grid(row=6,column=0,sticky="w",pady=8)
two=tk.Button(root,text="2",relief="sunken",width=10,height=3,fg="black",bg="grey",font=12,command=lambda:button_click(2))
two.grid(row=6,column=1,sticky="w",pady=8)
one=tk.Button(root,text="1",relief="sunken",width=10,height=3,fg="black",bg="grey",font=12,command=lambda:button_click(1))
one.grid(row=6,column=2,sticky="w",pady=8)
zero=tk.Button(root,text="0",relief="sunken",width=10,height=3,fg="black",bg="grey",font=12,command=lambda:button_click(0))
zero.grid(row=7,column=1,sticky="w",pady=8)
clear1=tk.Button(root,text="CLS",relief="sunken",width=10,height=3,fg="white",bg="#383A3A",font=12,command=clear)
clear1.grid(row=7,column=0,sticky="w",pady=8)
point=tk.Button(root,text="=",relief="sunken",width=10,height=3,fg="white",bg="#383A3A",font=12,command=button_equal)
point.grid(row=7,column=2,sticky="w",pady=8)
div=tk.Button(root,text="/",relief="sunken",width=10,height=3,fg="black",bg="goldenrod",font=12,command=button_div)
div.grid(row=7,column=3,sticky="w",pady=8)
plus=tk.Button(root,text="+",relief="sunken",width=10,height=3,fg="black",bg="goldenrod",font=12,command=button_add)
plus.grid(row=4,column=3,sticky="w",pady=8)
minus=tk.Button(root,text="-",relief="sunken",width=10,height=3,fg="black",bg="goldenrod",font=12,command=button_sub)
minus.grid(row=5,column=3,sticky="w",pady=8)
mul=tk.Button(root,text="X",relief="sunken",width=10,height=3,fg="black",bg="goldenrod",font=12,command=button_mul)
mul.grid(row=6,column=3,sticky="w",pady=8)

root.mainloop()