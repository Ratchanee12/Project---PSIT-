from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def instructionWindow(master):
    master.title("Instuction")  #ชื่อหน้าต่าง
    master.geometry("600x500") #ขนาดจอ
    master.option_add("*font", "Prompt 10 bold") #font
    canvas = Canvas(master, width=600, height=500) #สร้างจอขึ้นมา
    canvas.pack() #ใส่รูป
    photo = ImageTk.PhotoImage(Image.open('pic/in.png')) #รูปพื้นหลัง
    canvas.create_image(300, 250, image=photo) #สร้างจอขึ้นมาในรูป
    master.mainloop() # Execute tkinter
