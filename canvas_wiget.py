import tkinter as  tk
root=tk.Tk()
root.geometry("800x400")
root.title("canvas widget")
canvas_width=800
canvas_height=400
can_w=tk.Canvas(root,width=canvas_width,height=canvas_height)
can_w.pack()
can_w.create_line(0,400,800,0,fill="blue")
can_w.create_line(0,0,800,400,fill="green")
can_w.create_line(0,200,800,200,fill="purple")
can_w.create_line(400,400,400,0,fill="purple")
can_w.create_rectangle(2,2,110,100,fill="red")
can_w.create_rectangle(101,101,210,200,fill="green")
can_w.create_rectangle(202,202,310,300,fill="yellow")
can_w.create_rectangle(302,302,410,400,fill="sky blue")
can_w.create_text(30,10,text="all is well",fill="purple")
root.mainloop()