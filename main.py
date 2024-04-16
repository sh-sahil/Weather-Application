from tkinter import *
from tkinter import ttk
import json 
import requests


def data_get():
    city = cityName.get()
    dataRequest= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a08209fa92196cd7e2cf351184a87073")
    data = json.loads(dataRequest.content)
    
    #temperature
    y = data["main"]
    current_temp= int(y["temp"]-273.15)
    humidity = y["humidity"]
    tempMin = int(y["temp_min"]-273.15)
    tempMax = int(y["temp_max"]-273.15)
    pressure = y["pressure"]
    feels = int(y["feels_like"]-273.15)

    #name
    name = data["name"]

    climateLabel1.config(text = data["weather"][0]["description"])
    decsLabel1.config(text = data["weather"][0]["main"])
    
    #adding recieved info
    tempLabel1.configure(text=current_temp)
    tempLabelmin1.configure(text=tempMin)
    tempLabelmax1.config(text=tempMax)
    humidityLabel1.config(text=humidity)
    pressureLabel1.config(text=pressure)
    nameLabel1.config(text=name)
    feelslikeLabel1.config(text=feels)
    windspeedLabel1.config(text=str(data["wind"]["speed"]))
    if(current_temp < 25 ):
        cold = PhotoImage(file='cold1.png')
        coldLabel = Label(win,image = cold)
        coldLabel.place(x=110,y=180)
        coldLabel.config(bg="#1C9DE1")
    else:
        hot = PhotoImage(file='hot1.png')
        hotLabel = Label(win,image = hot)
        hotLabel.place(x=135,y=180)
        hotLabel.config(bg="#1C9DE1")
    visibilityLabel1.config(text = str(data["visibility"]))
  
            
win = Tk()
win.title("Weather App")
# path = PhotoImage(file = 'logo.png')
# win.iconphoto(False, path)
win.config(bg="#1C9DE1")
win.geometry("500x500")

nameLabel = Label(win,text="CHECK WEATHER",font=("TIMES NEW ROMAN",30,"bold"))
nameLabel.place(x=20,y=30,height=45,width=450)

searchAny = Label(win,text = "Select Any City name or Enter City Name :",font = ("TIMES NEW ROMAN",13))
searchAny.place(x = 20, y = 80)
searchAny.config(bg="#1C9DE1")

cityName = StringVar()
listName = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
comboBox = ttk.Combobox(win,values=listName,font=("TIMES NEW ROMAN",15,"bold"),textvariable = cityName)
comboBox.place(x=20,y=110, height=30, width= 300)

nameLabel1 = Label(win,text="",font=("TIMES NEW ROMAN",20,"bold"))
nameLabel1.place(x=30,y=145,height = 40)
nameLabel1.config(bg="#1C9DE1")

#temp
tempLabel1 = Label(win,text="",font=("TIMES NEW ROMAN",60,"bold"))
tempLabel1.place(x=30,y=190,height = 90, width = 90)
tempLabel1.config(bg="#1C9DE1")


#min temp
tempLabelmin = Label(win,text="Min Temperature(C)",font=("TIMES NEW ROMAN",15,"bold"))
tempLabelmin.place(x=225,y=180,height = 25)
tempLabelmin.config(bg="#1C9DE1")

tempLabelmin1 = Label(win,text="",font=("TIMES NEW ROMAN",15,"bold"))
tempLabelmin1.place(x=410,y=180,height = 30, width = 50)
tempLabelmin1.config(bg="#1C9DE1")

#max temp
tempLabelmax = Label(win,text="Max Temperature(C)",font=("TIMES NEW ROMAN",15,"bold"))
tempLabelmax.place(x=225,y=208,height = 25)
tempLabelmax.config(bg="#1C9DE1")

tempLabelmax1 = Label(win,text="",font=("TIMES NEW ROMAN",15,"bold"))
tempLabelmax1.place(x=410,y=204,height=40,width= 50)
tempLabelmax1.config(bg="#1C9DE1")

#feels like
feelslikeLabel= Label(win,text="Feels Like(C)",font=("TIMES NEW ROMAN",15,"bold"))
feelslikeLabel.place(x=225,y=235,height = 20)
feelslikeLabel.config(bg="#1C9DE1")

feelslikeLabel1 = Label(win,text="",font=("TIMES NEW ROMAN",15,"bold"))
feelslikeLabel1.place(x=410,y=237,height=20,width= 50)
feelslikeLabel1.config(bg="#1C9DE1")


#pressure
pressureLabel = Label(win,text="Pressure(mb)",font=("TIMES NEW ROMAN",15,"bold"))
pressureLabel.place(x=225,y=262,height = 20)
pressureLabel.config(bg="#1C9DE1")

pressureLabel1 = Label(win,text="",font=("TIMES NEW ROMAN",15,"bold"))
pressureLabel1.place(x=410,y=255,height=40,width= 50)
pressureLabel1.config(bg="#1C9DE1")


#humidity
humidityLabel = Label(win,text="Humidity(%)",font=("TIMES NEW ROMAN",15,"bold"))
humidityLabel.place(x=225,y=289,height = 20)
humidityLabel.config(bg="#1C9DE1")

humidityLabel1 = Label(win,text="",font=("TIMES NEW ROMAN",15,"bold"))
humidityLabel1.place(x=410,y=289,height=20,width= 50)
humidityLabel1.config(bg="#1C9DE1")

#Weather Desc
decsLabel = Label(win,text="WEATHER DESCRIPTION ",font=("TIMES NEW ROMAN",15,"bold"))
decsLabel.place(x=20,y=320,height = 40)
decsLabel.config(bg="#1C9DE1")

decsLabel1 = Label(win,text="",font=("TIMES NEW ROMAN",15,"bold"))
decsLabel1.place(x=300,y=320,height = 40)
decsLabel1.config(bg="#1C9DE1")

#climate
climateLabel = Label(win,text="WEATHER CLIMATE",font=("TIMES NEW ROMAN",15,"bold"))
climateLabel.place(x=20,y=350,height = 40)
climateLabel.config(bg="#1C9DE1")

climateLabel1 = Label(win,text="",font=("TIMES NEW ROMAN",15,"bold"))
climateLabel1.place(x=300,y=350,height = 40)
climateLabel1.config(bg="#1C9DE1")

#windSpeed
windspeedLabel = Label(win,text="WIND SPEED(KMPH)",font=("TIMES NEW ROMAN",15,"bold"))
windspeedLabel.place(x=20,y=380,height = 40)
windspeedLabel.config(bg="#1C9DE1")

windspeedLabel1 = Label(win,text="",font=("TIMES NEW ROMAN",15,"bold"))
windspeedLabel1.place(x=300,y=380,height = 40)
windspeedLabel1.config(bg="#1C9DE1")


doneButton = Button(win,text="SEARCH",font=("TIMES NEW ROMAN",15),command =data_get)
doneButton.place(x=350, y=112, height = 28, width = 100)



win.mainloop()







