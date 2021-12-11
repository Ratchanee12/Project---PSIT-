import tkinter as tk
import requests
import time
 

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

    final_info = condition + "\n" + des + "\n"+ str(temp) + "°C" # สภาพอากาศแล้วตามด้วยอุณหภูมิ
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

    #try:
    #    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=")
 #       api = json.loads(api_request.content)
#        city : api[0][' ReportingArea']
 #       quality = api[0][' AQI']
 #       condition = api[0][ 'Category'][ 'Name']

 #       if condition == "Clouds":
  #          weather_color = "#OCe"
 #       elif condition == "Moderate":
  #          weather_color = "#FFFFOe"
  #      elif condition == "Unhealthy for Sensitive Groups":
  #          weather_color = "#ff9900"
  #      elif condition == "Unhealthy":
  #          weather_color = "#FFee0e"
  #      elif condition == "Very Unhealthy":
  #          weather_color = "#990066"
  #      elif condition == "Hazardous":
   #         weather_color = "#660009"


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.config(background="#D4E2D4")
f = ("Prompt", 16, "bold")
t = ("Prompt", 30, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack() # แสดงข้อความลงบนหน้าจอ
label1.config(background="#D4E2D4")
label2 = tk.Label(canvas, font=f)
label2.pack() # แสดงข้อความลงบนหน้าจอ
label2.config(background="#D4E2D4")
canvas.mainloop()
