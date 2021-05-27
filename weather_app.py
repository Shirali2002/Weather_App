from tkinter import *
import requests
import time


def get_weather(window):
    city = entry_city.get()
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=a4268b8e63c13c18c3dfad2472682603"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise']-21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset']-21600))

    final_info = f'{condition}\n{str(temp)}°C'
    final_data = f'\nMax Temp: {str(max_temp)}\n' \
                 f'Min Temp: {str(min_temp)}\n' \
                 f'Pressure: {str(pressure)}\n' \
                 f'Humidity: {str(humidity)}\n' \
                 f'Wind speed: {str(wind)}\n' \
                 f'Sunrise: {sunrise}\n' \
                 f'Sunset: {sunset}'

    label_1.config(text=final_info)
    label_2.config(text=final_data)


window = Tk()
window.geometry('600x500')
window.title('Weather App')

font_1 = ('poppins', 15, 'bold')
font_2 = ('poppins', 25, 'bold')

entry_city = Entry(window, justify=CENTER, font=font_1)
entry_city.pack(pady=20, ipadx= 150)
entry_city.focus()
entry_city.bind('<Return>', get_weather)

label_1 = Label(window, font=font_1)
label_1.pack()
label_2 = Label(window, font=font_2)
label_2.pack()


window.mainloop()