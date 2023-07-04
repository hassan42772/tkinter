import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()
root.title("IMAGE MANAGING")
root.geometry("1300x1300") 

root.configure(background="white")
root.iconbitmap(r'img.ico') 

image1=Image.open("img1.jpg")
image2=Image.open("img2.jpg")
image3=Image.open("img3.jpg")
image4=Image.open("img4.jpg")
image5=Image.open("img5.jpg")
image6=Image.open("pic.jpg")
image7=Image.open("image7.jpg")
image1=image1.resize((200,200), resample=Image.Resampling.LANCZOS)
image1=ImageTk.PhotoImage(image1)
image2=image2.resize((200,200), resample=Image.Resampling.LANCZOS)
image2=ImageTk.PhotoImage(image2)
image3=image3.resize((200,200), resample=Image.Resampling.LANCZOS)
image3=ImageTk.PhotoImage(image3)
image4=image4.resize((600,600), resample=Image.Resampling.LANCZOS)
image4=ImageTk.PhotoImage(image4)
image5=image5.resize((200,200), resample=Image.Resampling.LANCZOS)
image5=ImageTk.PhotoImage(image5)
image6=image6.resize((200,200), resample=Image.Resampling.LANCZOS)
image6=ImageTk.PhotoImage(image6)
image7=image7.resize((400,400), resample=Image.Resampling.LANCZOS)
image7=ImageTk.PhotoImage(image7)
# frames
frame1=tk.Frame(root,background="white")
frame1.grid(column=0,row=0)

frame2=tk.Frame(root,background="white")
frame2.grid(column=1,row=0,rowspan=2)

frame3=tk.Frame(root,background="white")
frame3.grid(column=2,row=0,sticky="nw")

frame4=tk.Frame(root,background="white")
frame4.grid(column=2,rows=1,sticky="w")
# labels
label1=tk.Label(frame1,image=image1)
label1.grid(column=0,row=0,sticky="w")

label2=tk.Label(frame1,image=image2)
label2.grid(column=0,row=1,sticky="w")

label3=tk.Label(frame1,image=image3)
label3.grid(column=0,row=2,sticky="w")

label4=tk.Label(frame2,image=image4)
label4.grid(column=0,row=0)

label5=tk.Label(frame3,image=image5)
label5.grid(column=0,row=0,sticky="w")

label6=tk.Label(frame3,image=image6)
label6.grid(column=1,row=0,sticky="w")

label7=tk.Label(frame3,image=image7)
label7.grid(column=0,row=1,columnspan=2)




root.mainloop()