import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600


def test_function(entry):
    print('This is the entry:', entry)

#    507ee44243772f664f37304f3f708fc0
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}


def get_weather(city):
    weather_key = '507ee44243772f664f37304f3f708fc0'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Matric'}
    response = requests.get(url, params=params)
    print(response.json())


window = tk.Tk()

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

backImage = tk.PhotoImage(file='test1.png')
backLabel = tk.Label(window, image=backImage)
backLabel.place(relwidth=1, relheight=1)

frame = tk.Frame(window, bg='#f5a742', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Get Weather", font=40,
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

lower_frame = tk.Frame(window, bg='#f5a742', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

window.mainloop()
