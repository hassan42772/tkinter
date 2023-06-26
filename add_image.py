import tkinter as tk
from  PIL import Image,ImageTk
import random as rm
import emoji
root=tk.Tk()
root.geometry("400x450")
# root.minsize(800,600)
# root.maxsize(800,600)
root.title("LEGEND PROFILE")
root.iconbitmap(r"C:/Users/GH/OneDrive/Desktop/codes/tkinter/img.ico")
global images
def button_click():
    global images
    imgs=[images1,images2,images3,images4,images5,images6]
    images=rm.choice(imgs)
    images_label.configure(image=images)
# frame
master_frame= tk.Frame(root,bg="#BCC3C9")
master_frame.pack(fill="both",expand=True)
# text label
text_label=tk.Label(master_frame,text=f"LEGEND \n PROFILE PIC \U0001F923",font=("'Arial', 24"),fg="black",bg="#697B8B")
text_label.pack()
# images
images1=Image.open("img1.jpg")
images1=images1.resize((250,250),resample=Image.Resampling.LANCZOS)
images1=ImageTk.PhotoImage(images1)
images2=Image.open("img2.jpg")
images2=images2.resize((250,250),resample=Image.Resampling.LANCZOS)
images2=ImageTk.PhotoImage(images2)
images3=Image.open("img3.jpg")
images3=images3.resize((250,250),resample=Image.Resampling.LANCZOS)
images3=ImageTk.PhotoImage(images3)
images4=Image.open("img4.jpg")
images4=images4.resize((250,250),resample=Image.Resampling.LANCZOS)
images4=ImageTk.PhotoImage(images4)
images5=Image.open("img5.jpg")
images5=images5.resize((250,250),resample=Image.Resampling.LANCZOS)
images5=ImageTk.PhotoImage(images5)
images6=Image.open("img6.jpg")
images6=images6.resize((250,250),resample=Image.Resampling.LANCZOS)
images6=ImageTk.PhotoImage(images6)
images=[images1,images2,images3,images4,images5,images6]
# image label
images_label=tk.Label(master_frame,image=images1)
images_label.pack(pady=20)
# button
click_button = tk.Button(master_frame,font=("'Arial', 24 "),width=13,text="PRESS!" ,fg="black",bg="#697B8B",relief="sunken",command=button_click)
click_button.pack()




root.mainloop()
