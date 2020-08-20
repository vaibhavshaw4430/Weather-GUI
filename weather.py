import tkinter as tk
import requests
from tkinter import font
HEIGHT = 400
WIDTH = 800

def test_func(entry):
	print("this is the entry",entry)
#api.openweathermap.org/data/2.5/forecast?q={city name},{state},{country code}&appid={your api key}
#ce42751eb1ac79149c0c11c35ea3d09d

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature(*F): %s' % (name,desc,temp)
	except:
		final_str = 'THERE WAS A PROBLEM'

	return final_str

def get_weather(city):
	weather_key = 'ce42751eb1ac79149c0c11c35ea3d09d'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q':city, 'units': 'imperial'}
	response = requests.get(url,params=params)
	weather = response.json()

	label['text'] = format_response(weather)
	print(weather['name'])
	print(weather['weather'][0]['description'])
	print(weather['main']['temp'])

	
root = tk.Tk()
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='image\\hi.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg='blue',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75, relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=('Courier',15))
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text ="Get Weather",font=30,command=lambda: get_weather(entry.get()))
button.place(relx=0.7,rely=0,relwidth=0.3,relheight=1)

lower_frame = tk.Frame(root,bg='blue',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame,bg='white',font=('Courier',18),anchor='nw',justify='left',bd=4)
label.place(relwidth=1,relheight=1)


root.mainloop()
