import tkinter as tk
import pygame
from pygame import mixer
pygame.init()
root=tk.Tk()
root.geometry("400x440")

def play():
    mixer.music.load('Dil Pe Zakham Khatay Hain Lyrical Song By Nusrat Fateh.mp3')
    mixer.music.play()
def stop():
    mixer.music.load('Dil Pe Zakham Khatay Hain Lyrical Song By Nusrat Fateh.mp3')
    mixer.music.stop()
def pause():
    mixer.music.pause()
def unpause():
    mixer.music.unpause()



click_button = tk.Button(root,font=("'Arial', 10 "),width=15,height=2,text="play" ,fg="black",bg="#697B8B",relief="sunken",command=play)
click_button.grid(column=0,row=0,pady=20)
click_button1 = tk.Button(root,font=("'Arial', 10 "),width=15,height=2,text="stop" ,fg="black",bg="#697B8B",relief="sunken",command=stop)
click_button1.grid(column=0,row=1,pady=20)
click_button2 = tk.Button(root,font=("'Arial', 10 "),width=15,height=2,text="pasue" ,fg="black",bg="#697B8B",relief="sunken",command=pause)
click_button2.grid(column=0,row=2,pady=20)
click_button3 = tk.Button(root,font=("'Arial', 10 "),width=15,height=2,text="unpause" ,fg="black",bg="#697B8B",relief="sunken",command=unpause)
click_button3.grid(column=0,row=3,pady=20)


root.mainloop()