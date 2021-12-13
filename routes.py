from instruction import *
from weather import *
from tkinter import messagebox

#หน้าเชื่อมต่อทั้งหมด

class WindowRoute:
    def __init__(self, master):
        self.master = master

    # สร้างหน้าต่างแอปพลิเคชั่น
    def weatherapp(self):
        self.master.lower()  #ยุบหน้าจอแรกลง (master คือ หน้าต่าง main menu)
        self.master.attributes('-topmost', 0) #ปรับลำดับหน้าจอลงให้ต่ำสุดหรืออยู่ข้างล่าง
        self.newWindow = Toplevel(self.master) #สร้างหน้าใหม่ขึ้นมาซ้อนไว้
        self.newWindow.protocol("WM_DELETE_WINDOW", self.on_backing)  #เมื่อมีการปิดหน้าต่างให้ เรียกฟังก์ชัน on_backing ของ class นี้
        WeatherAppWindow(self.newWindow) # เรียกฟังก์ชัน WeatherAppWindow เพื่อแสดงแอปพลิเคชั่น
    
    # สร้างหน้าต่างวิธีการใช้งานแอปพลิเคชั่น
    def instruction(self):
        self.master.lower()  #ยุบหน้าจอแรกลง (master คือ หน้าต่าง main menu)
        self.master.attributes('-topmost', 0) #ปรับลำดับหน้าจอลงให้ต่ำสุดหรืออยู่ข้างล่าง
        self.newWindow = Toplevel(self.master) #สร้างหน้าใหม่ขึ้นมาซ้อนไว้
        self.newWindow.protocol("WM_DELETE_WINDOW", self.on_backing)  #เมื่อมีการปิดหน้าต่างให้ เรียกฟังก์ชัน on_backing ของ class นี้
        instructionWindow(self.newWindow) #เรียกฟังก์ชัน instructionWindow เพื่อแสดงผลหน้าต่างวิธีการใช้งาน App

    # event สำหรับกลับไปจอ main menu
    def on_backing(self):
        self.master.lift()  #ขยายหรือนำหน้าจอ main menu กลับขึ้นมา
        self.master.attributes('-topmost', 1) #ปรับลำดับหน้าจอ main menu ลงให้ขึ้นมาบนสุด
        self.newWindow.destroy() #ทำลายหรือปิดหน้าต่างที่เปิดอยู่

    # ปิดโปรแกรมด้วย Destroy
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"): #สร้างหน้าจอถาม ให้ยืนยันก่อนปิดหน้าต่าง
            self.master.destroy() #ปิดโปรแกรม
