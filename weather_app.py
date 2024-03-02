import requests
from tkinter import *

def data_fectching():
    city_name = city_n.get()
    API_key = 'f1bf8c307c232ebf02e5853ec18e8fb1'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{0},{0}&appid={API_key}&units=metric"

    response = requests.get(url)
    if response.status_code==200:
        data =response.json()
        temp1.config(text=f"{data['main']['temp']}°C")
        min_temp1.config(text=f"{data['main']['temp_min']}°C")
        max_temp1.config(text=f"{data['main']['temp_max']}°C")
        humidity1.config(text=f"{data['main']['humidity']}%")
        description1.config(text=f"{data['weather'][0]['description']}")

window=Tk()
window.title("Weather App")
window.config(background="dark blue")
window.minsize(height=450,width=500)

logo=Label(text="WEATHER APP",fg="gold",font=("helvetica",30),background="dark blue")
logo.grid(column=0,row=0,columnspan=3,padx=10,pady=10)

city=Label(text="Enter the city name :",background="light blue",width=25,padx=10,pady=10)
city.grid(column=0,row=1)

city_n=Entry(width=40)
city_n.grid(column=2,row=1,padx=10,pady=10)

submit=Button(text="Check Weather",command=data_fectching,width=30,background="gold")
submit.grid(column=0,row=2,padx=10,pady=10,columnspan=3)

temp=Label(text="Temperature :",background="light blue",width=25,padx=10,pady=10)
temp.grid(column=0,row=3)

min_temp=Label(text="Minimum Temperature :",background="light blue",width=25,padx=10,pady=10)
min_temp.grid(column=0,row=4,padx=10,pady=10)

max_temp=Label(text="Maximum Temperature :",background="light blue",width=25,padx=10,pady=10)
max_temp.grid(column=0,row=5,padx=10,pady=10)

humidity=Label(text="Humidity :",background="light blue",width=25,padx=10,pady=10)
humidity.grid(column=0,row=6,padx=10,pady=10)

description=Label(text="Description :",background="light blue",width=25,padx=10,pady=10)
description.grid(column=0,row=7,padx=10,pady=10)

temp1=Label(text="---",fg="white",background="dark blue",font=("helvetica",20))
temp1.grid(column=2,row=3)

min_temp1=Label(text="---",fg="white",background="dark blue",font=("helvetica",20))
min_temp1.grid(column=2,row=4)

max_temp1=Label(text="---",fg="white",background="dark blue",font=("helvetica",20))
max_temp1.grid(column=2,row=5)

humidity1=Label(text="---",fg="white",background="dark blue",font=("helvetica",20))
humidity1.grid(column=2,row=6)

description1=Label(text="---",fg="white",background="dark blue",font=("helvetica",20))
description1.grid(column=2,row=7)

window.mainloop()