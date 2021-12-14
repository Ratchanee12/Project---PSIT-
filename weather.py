import tkinter as tk
import requests
import time
from tkinter import *
from PIL import Image, ImageTk

# Create object 
def WeatherAppWindow(master):
    #master = tk() ใส่แล้วจะเกิดจอขาว
    master.title("Weather Application")  # ชื่อแอป
    master.geometry("600x500") # Adjust size 
    master.option_add("*font", "Prompt 10 bold") #font
    master.config(background="#FCF8E8") #bg
    f = ("Prompt", 15, "bold")
    b = ("Prompt", 18, "bold")
    t = ("Prompt", 24, "bold")
    textField = tk.Entry(master, justify='center', width = 20, font = t) #ให้ค่าที่ใส่อยู่ตรงกลาง
    textField.pack(pady = 20) #ใส่ตำแหน่งพิกัด y
    textField.focus() #focus() เมื่อสั่งคำสั่งจะพบว่า cursor ของ mouse มักจะไปอยู่หน้า input
    

    def getWeather(canvas):
        city = textField.get() # ใส่ชื่อเมือง
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

        json_data = requests.get(api).json() # ดึงข้อมูล json มาใช้
        condition = json_data['weather'][0]['main'] # ดึงข้อมูลสภาพอากาศจาก Array ใน Json มาใช้
        des = json_data['weather'][0]['description'] # ดึงข้อมูลสภาพอากาศจาก Array ใน Json มาใช้
        temp = int(json_data['main']['temp'] - 273.15) # ดึงข้อมูลอุณหภูมิ ณ เวลานั้นจาก Array ใน Json มาใช้ แล้วทำให้เป็นเซลเซียส
        min_temp = int(json_data['main']['temp_min'] - 273.15) # ดึงข้อมูลอุณหภูมิต่ำสุด จาก Array ใน Json มาใช้ 
        max_temp = int(json_data['main']['temp_max'] - 273.15) # ดึงข้อมูลอุณหภูมิสูงสุด จาก Array ใน Json มาใช้ 
        pressure = json_data['main']['pressure'] #ดึงข้อมูลความกดอากาศจาก Array ใน Json มาใช้
        humidity = json_data['main']['humidity'] #ดึงข้อมูลความชื้นอากาศจาก Array ใน Json มาใช้
        wind = json_data['wind']['speed'] #ดึงข้อมูลความเร็วลมจาก Array ใน Json มาใช้
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600)) #ดึงข้อมูลเวลาพระอาทิตย์ขึ้นจาก Array ใน Json มาใช้
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600)) #ดึงข้อมูลเวลาพระอาทิตย์ตกจาก Array ใน Json มาใช้

        final_info = condition # สภาพอากาศ
        final_between = des + "\n" + str(temp) + "°C" # สภาพอากาศแล้วตามด้วยอุณหภูมิ
        final_data = "Min temperature: " + str(min_temp) + "°C" + "\n" + "Max temperature: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
        label1.config(text = final_info) #เชื่อมต่อให้แสดงผลค่าที่รับมา
        label3.config(text = final_between) #เชื่อมต่อให้แสดงผลค่าที่รับมา
        label2.config(text = final_data) #เชื่อมต่อให้แสดงผลค่าที่รับมา

    label1 = tk.Label(master, font=t, fg='#483434') # สร้างกรอบข้อความที่จะแสดงขึ้นมา
    label1.pack() # แสดงข้อความลงบนหน้าจอ
    label1.config(background="#EADCA6", width=13, height=2) #กำหนดสีพื้นหลังและขนาดกรอบ
    label3 = tk.Label(master, font=b, fg='#483434') # สร้างกรอบข้อความที่จะแสดงขึ้นมา
    label3.pack() # แสดงข้อความลงบนหน้าจอ
    label3.config(background="#E2C275", width=17, height=3) #กำหนดสีพื้นหลังและขนาดกรอบ
    label2 = tk.Label(master, font=f, fg='white') # สร้างกรอบข้อความที่จะแสดงขึ้นมา
    label2.pack() # แสดงข้อความลงบนหน้าจอ
    label2.config(background="#C36A2D", width=21, height=9) #กำหนดสีพื้นหลังและขนาดกรอบ
    textField.bind('<Return>', getWeather) # รีเทิร์นค่ากลับไปที่ fuction
    master.mainloop() # Execute tkinter
