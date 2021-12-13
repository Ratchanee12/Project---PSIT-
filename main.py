from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from routes import *


def menu():
    """Weather Appication"""
    root = Tk()  #สร้างหน้าต่าง
    root.title("Weather Application")  #ชื่อแอปพลิเคชั่น
    root.geometry("600x500")  #ขนาดจอหลัก
    root.option_add("*font", "Prompt 10 bold") #font
    canvas = Canvas(root, width=600, height=500) #สร้างจอขึ้นมาในรูป
    canvas.pack() #ใส่รูป
    
    photo = ImageTk.PhotoImage(Image.open('pic/background.png')) #แทรกรูปขึ้นมาใน canvas
    canvas.create_image(300, 250, image=photo) #กำหนดตำแหน่งของรูปที่จะอยู่

    appTitle = Label(root, text="Weather Application", bg='#b3e4fb', fg='#7267CB', font=("Prompt", 30, 'bold')) #Head title
    canvas.create_window(300, 70, anchor='center', window=appTitle) #ใส่ font ลงไปใน canvas

    route = WindowRoute(root) #เชื่อมหน้า
    startBtnImg = ImageTk.PhotoImage(Image.open('pic/btn3.png'))
    startBtn = Button(root, text="Start", bg='#b3e4fb', image=startBtnImg , borderwidth=0, command=route.weatherapp, anchor='center') #เชื่อมปุ่มไปยังหน้าแอปพลิเคชั่น
    canvas.create_window(300, 200, anchor='center', window=startBtn) #ใส่ปุ่มลงไปใน canvas

    quitBtnImg = ImageTk.PhotoImage(Image.open('pic/logout_btn4.png'))
    quitBtn = Button(root, text="logout", image=quitBtnImg , borderwidth=0, command=route.on_closing, anchor='center') #เชื่อมปุ่มไปหน้า pop up คำถามจะปิดหน้าต่างไหม
    canvas.create_window(550, 450, anchor='center', window=quitBtn) #ใส่ปุ่มลงไปใน canvas
    
    nextBtnImg = ImageTk.PhotoImage(Image.open('pic/book_btn1.png'))
    nextBtn = Button(root, text="book", image=nextBtnImg , borderwidth=0, command=route.instruction, anchor='s') #เชื่อมปุ่มไปยังหน้าคู่มือ
    canvas.create_window(50, 485, anchor='s', window=nextBtn) #ใส่ปุ่มลงไปใน canvas

    root.protocol("WM_DELETE_WINDOW", route.on_closing) # on close window
    root.mainloop()  # Execute tkinter

menu()