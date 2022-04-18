from tkinter import *


from database_file import Detail

import tkinter as tk
from geopy.geocoders import Nominatim

from tkinter import ttk,messagebox

from timezonefinder import TimezoneFinder

from datetime import datetime

import requests

import pytz

root=Tk()
root.title("Weather-App")

root.geometry("900x500+300+200")



root['bg']='white';



#new_wind=0;



# FUNCTIONS 
new_wind=0
i=0
check=False


# This will create style object
#style = Style()

#style.configure('W.TButton', font =('calibri', 10, 'bold', 'underline'),foreground = 'red')
#obj12 = Detail()

def get_weather():
    #print("inside new wind is ",new_wind)
    city=text_field.get()
    print("city is ",city)
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    print("locations is ",location)
    result=obj.timezone_at(lng=location.longitude, lat=location.latitude)

    print(result) # it prints the timezone of selected city
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")

    clock.config(text=current_time)
    name.config(text="Current Time")
    
    
    
    
    
    weather_key='1dcc97cd56197a5947b301ed4f3564f8'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperical'} 
    response=requests.get(url,params)
    print(response.json())
    
    #weather inside get_weather
    
   # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    
   # api key 1dcc97cd56197a5947b301ed4f3564f8
   
   # api  https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
   
   
     
    
    #api="https://api.openweathermap.org/data/2.5/weather?lat="+city+"&1dcc97cd56197a5947b301ed4f3564f8"
    
    
    #json_data=requests.get(api).json()
    condition = response.json()['weather'][0]['main']
    description=response.json()['weather'][0]['description']
    temp=int(response.json()['main']['temp']-273.15)
    pressure=response.json()['main']['pressure']
    humidity=response.json()['main']['humidity']
    wind=response.json()['wind']['speed']
    
    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","Feels","Like",temp,"°"))
    
    print("wind is ",wind)
    global new_wind
    
    global check
    check=True
    new_wind=wind;
    
    print("new_wind23154 is ",new_wind)
    print("city name is ",city)
    print("type of city name is ",type(city))
    print("new wind type is ",type(new_wind))
    print("temp is ",temp)
    print("Type of temp is ",type(temp))
    print("pressure is",pressure)
    print("type of pressure is",type(pressure))
    print("humadity is ",humidity)
    print("type of humadity is",type(humidity))
    print("current time is ",current_time)
    print("type of current time is",type(current_time))
    
    w.config(text=wind)
    
    get_wind=wind
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)
    
    
    def save_at_server():
        a=messagebox.askquestion("askquestion", "Are you sure to save data on server?")
        if(a):
            import pyodbc
            con = pyodbc.connect("driver={SQL Server};Server=Sanju;database=weather;uid=sa;pwd=5911")
            cur = con.cursor()
            cur.execute("Insert into detail2 values(?,?,?,?,?,?)",city,current_time,temp,pressure,wind,humidity)
            con.commit()
            print("recorrd added")
            
            """    
            cur.execute("Select * From detail2")
            records = cur.fetchall()
            print("records ",records)
            print("Type of records is ",type(records))
            global i
            
            #obj=Detail(i,i,city,current_time,temp,pressure,wind,humidity)
            i=0
            #obj=Detail()
            for record in records:
                #print("Records is ")
                print(record[0],record[1],record[2],record[3],record[4],record[5])
                obj12.add(i, record[0], record[1], record[2], record[3], record[4], record[5], record[6])
                i+=1
            """
    bt1=Button(root,bd=2,borderwidth=0,text="save at server",height=2,width=12,bg="black",fg="white",font="Helvetica",command=save_at_server)
    
    bt1.place(x=700,y=200)
    
        
# TIME 
 



name=Label(root,font=("arial",15,"bold"))
name['bg']='white';
name.place(x=22,y=100)
clock=Label(root,font=("Helvetica",20))
clock['bg']='white';
clock.place(x=30,y=130)




# SEARCH BOX

Search_image=PhotoImage(file="./Images/search.png")
my_image=Label(image=Search_image)
my_image['bg']='white';
my_image.place(x=20,y=20)

# TEXT FIELD FOR SEARCH

text_field=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
text_field.place(x=50,y=40)
text_field.focus()


# SEARCH-ICON

Search_icon=PhotoImage(file="./Images/search_icon.png")
my_search_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=get_weather)
my_search_icon.place(x=400,y=34)



# LOGO IMAGE

Logo_image=PhotoImage(file="./Images/logo.png")
logo=Label(image=Logo_image)
logo['bg']='white';
logo.place(x=150,y=100)


# BOTTOM BOX

Frame_image=PhotoImage(file="./Images/box.png")

frame_image=Label(root,image=Frame_image)
frame_image['bg']='white';


frame_image.pack(padx=10,pady=5,side=BOTTOM)


# EXTRA LABELS LIKE WIND ETC


get_wind=tk.IntVar()

label1=Label(root,text="Wind",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="Humadity",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)


label3=Label(root,text="Description",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=435,y=400)


label4=Label(root,text="Pressure",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)





t=Label(font=("arial",70,"bold"),fg="#ee666d")
t['bg']='white';
t.place(x=400,y=150)



c=Label(font=("arial",15,"bold"))
c['bg']='white';
c.place(x=400,y=250)




w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)



h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)



d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)




p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


button_mode=True

def customize():
    global button_mode
    if(button_mode):
        theme_button.config(image=off,bg="black",activebackground="black")
        root.config(bg="black")
        # changing black buttons
        name['fg']='white';
        clock['fg']='white';
        c['fg']='white';
        name['bg']='black';
        clock['bg']='black';
        my_image['bg']='black';
        logo['bg']='black';
        frame_image['bg']='black';
        
        t['bg']='black';
        c['bg']='black';
        
       # label1['fg']='black';
        button_mode=False
    else:
        theme_button.config(image=on,bg="white",activebackground="white")
        root.config(bg="white")
        
        name['fg']='black';
        clock['fg']='black';
        c['fg']='black';
        
        name['bg']='white';
        clock['bg']='white';
        my_image['bg']='white';
        logo['bg']='white';
        frame_image['bg']='white';
        t['bg']='white';
        c['bg']='white';
        button_mode=True




#Frame_image=PhotoImage(file="./Images/box.png")
on=PhotoImage(file="./Images/light.png")
off=PhotoImage(file="./Images/dark.png")

#on.place(x=300,y=50)
theme_button=Button(root,image=on,bg="white",activebackground="white",borderwidth=0,command=customize)

theme_button.place(x=600,y=34)

#new_button=Button

#  DARK THEME  BUTTON CODING



#  DARK THEME  BUTTON CODING





# about database 



print("Get wind is ",get_wind)
print("new wind567 is ",new_wind)


def show_all():
    import pyodbc
    con = pyodbc.connect("driver={SQL Server};Server=Sanju;database=weather;uid=sa;pwd=5911")
    cur = con.cursor()
    #cur.execute("Insert into detail2 values(?,?,?,?,?,?)",city,current_time,temp,pressure,wind,humidity)
    #con.commit()
    
    print("recorrd fetched")
    cur.execute("Select * From detail2")
    records = cur.fetchall()
    print("records ",records)
    print("Type of records is ",type(records))
    global i
            
    #obj=Detail(i,i,city,current_time,temp,pressure,wind,humidity)
    i=0
    obj12=Detail()
    for record in records:
        print("recorsd",record)
        print("hello")
        print(record[0],record[1],record[2],record[3],record[4],record[5])
        obj12.add(i, record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        i+=1
    
    obj12.show()
    
    
root.resizable(False,False)

bt2=Button(root,bd=2,borderwidth=0,text="show database",height=2,width=12,bg="black",fg="white",font="Helvetica",command=show_all)
bt2.place(x=700,y=300)
    

root.mainloop()