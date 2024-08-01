from tkinter import *
from PIL  import ImageTk,Image
from tkinter import font
from tkinter import ttk
import time
from datetime import datetime
from Tree import Tree
from tkinter.messagebox import *
import binary
from car_sql import *


wind=Tk()
wind.geometry(f'750x550+{350}+{100}')
wind.resizable(False,False)
wind.iconbitmap('icon.ico')
wind.title('CAR RENTAL SYSYTEM')
can=Canvas(wind,width=750,height=550)
can.pack()
img=Image.open('main1.jpg')
resized=img.resize((750,550))
final_img=ImageTk.PhotoImage(resized)
can.create_image(0,0,image=final_img,anchor='nw')

def addvehicle():

    def update1():
        it=vehicle_id()
        add_vehicle(it,model.get(),make.get(),int(yea.get()),float(rate.get()),int(seat.get()),Ac.get())
    #'VehicleID', 'Model', 'Make', 'Year', 'RentalRate','Seat','AC'
    can2=Canvas(wind,bg='white',width=460,height=300)
    can.create_window(150,60,window=can2,anchor='nw')

    can2.create_text(120,85,text='Model: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,125,text='Make: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,165,text='Year: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,205,text='RentalRate: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,245,text='Seating Capacity: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,285,text='AC: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    model=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    make=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    yea=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    rate=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    seat=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    Ac=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    upd_button=Button(wind,text='Update',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=update1)
    back_button=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=lambda: can2.destroy())
    
    # item.insert(0,data[1])
    # quty.insert(0,data[2])
    # cost.insert(0,data[-1])
    
    can2.create_window(200,70,window=model,anchor='nw')
    can2.create_window(200,110,window=make,anchor='nw')
    can2.create_window(200,150,window=yea,anchor='nw')
    can2.create_window(200,190,window=rate,anchor='nw')
    can2.create_window(200,230,window=seat,anchor='nw')
    can2.create_window(200,270,window=Ac,anchor='nw')
    can2.create_window(340,20,window=upd_button,anchor='nw')
    can2.create_window(340,250,window=back_button,anchor='nw')
def delvehicle():
    def update1():
        delete_vehicle(vid.get())        
    can2=Canvas(wind,bg='white',width=460,height=300)
    can.create_window(150,60,window=can2,anchor='nw')
    can2.create_text(120,90,text='Delete Vehicle',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    vid=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    can2.create_window(200,110,window=vid,anchor='nw')
    upd_button=Button(wind,text='Update',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=update1)
    back_button=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=lambda: can2.destroy())
    can2.create_window(300,20,window=upd_button,anchor='nw')
    can2.create_window(300,250,window=back_button,anchor='nw')
def rented_vehicle():

    can1 =Canvas(wind,bg='white',width=650,height=370)
    can.create_window(40,155,anchor='nw',window=can1)

    bill=Tree(wind)
    bill.get_tree().config(column=['c{}'.format(i+1) for i in range(5)],show='headings')
    bill.create_headings(['RentalID', 'CustomerID', 'VehicleID', 'RentalDate', 'ReturnDate'])
    bill.delete()
    req_data=display_rental()
    print(req_data)
    if len(req_data)>=4:
        bill.get_tree().config(height=4)
    else:
        bill.get_tree().config(height=len(req_data))
    bill.add_datas(req_data)
    
    can1.create_window(50,140,window=bill.get_tree(),anchor='nw')

    back=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='tomato3',foreground='white',command=lambda:can1.destroy())
    can1.create_window(265,290,window=back,anchor='nw')

def displayvehicle():
    

    can1 =Canvas(wind,bg='white',width=650,height=370)
    can.create_window(40,155,anchor='nw',window=can1)
    bill=Tree(wind)
    bill.get_tree().config(column=['c{}'.format(i+1) for i in range(7)],show='headings')
    bill.create_headings(['VehicleID', 'Model', 'Make', 'Year', 'RentalRate','Seating Capacity',"Ac"])
    bill.delete()
    req_data=display_vehicle()
    if len(req_data)>=4:
        bill.get_tree().config(height=4)
    else:
        bill.get_tree().config(height=len(req_data))
    bill.add_datas(req_data)
    
    can1.create_window(-50,140,window=bill.get_tree(),anchor='nw')

    back=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='tomato3',foreground='white',command=lambda:can1.destroy())
    can1.create_window(265,290,window=back,anchor='nw')
    
def delrented():
    def update1():
        print(type(rid.get()))
        delete_rental(rid.get())        
    can2=Canvas(wind,bg='white',width=460,height=300)
    can.create_window(150,60,window=can2,anchor='nw')
    can2.create_text(120,90,text='Delete Rental vehicle',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    rid=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    can2.create_window(200,110,window=rid,anchor='nw')
    upd_button=Button(wind,text='Update',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=update1)
    back_button=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=lambda: can2.destroy())
    can2.create_window(300,20,window=upd_button,anchor='nw')
    can2.create_window(300,250,window=back_button,anchor='nw')

def rentalhistory():
    can1 =Canvas(wind,bg='white',width=650,height=370)
    can.create_window(40,155,anchor='nw',window=can1)
    bill=Tree(wind)
    bill.get_tree().config(column=['c{}'.format(i+1) for i in range(7)],show='headings')
    bill.create_headings(['RentalID' ,'CustomerID','VehicleID','RentalDate','ReturnDate','TotalCost','DeletedDate'])
    bill.delete()
    req_data=display_rental_history()
    if len(req_data)>=4:
        bill.get_tree().config(height=4)
    else:
        bill.get_tree().config(height=len(req_data))
    bill.add_datas(req_data)
    
    can1.create_window(0,140,window=bill.get_tree(),anchor='nw')

    back=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='tomato3',foreground='white',command=lambda:can1.destroy())
    can1.create_window(265,290,window=back,anchor='nw')

def displaycust():
    can1 =Canvas(wind,bg='white',width=650,height=370)
    can.create_window(40,155,anchor='nw',window=can1)
    bill=Tree(wind)
    bill.get_tree().config(column=['c{}'.format(i+1) for i in range(6)],show='headings')
    bill.create_headings(['CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address'])
    bill.delete()
    req_data=display_customer()
    if len(req_data)>=4:
        bill.get_tree().config(height=4)
    else:
        bill.get_tree().config(height=len(req_data))
    bill.add_datas(req_data)
    
    can1.create_window(0,140,window=bill.get_tree(),anchor='nw')

    back=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='tomato3',foreground='white',command=lambda:can1.destroy())
    can1.create_window(265,290,window=back,anchor='nw')

def logout():
    wind.destroy()
    import intro2
    
    
can.create_text(257,10,text='Car Rental Manager',anchor='nw',fill='navyblue',font=font.Font(family='Ailza Bright Demo',weight='bold',size=25,underline=1),)
can.create_text(260,10,text='Car Rental Manager',anchor='nw',fill='white',font=font.Font(family='Ailza Bright Demo',weight='bold',size=25),)

can.create_text(370,100,text='What are you looking for?? ',font=font.Font(family='Ailza Bright Demo',size=18,weight='bold'),fill='navyblue')

b0=Button(wind,text='Display Customer',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=displaycust)
can.create_window(300,130,window=b0,anchor='nw')

b1=Button(wind,text='Display Vehicle',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=displayvehicle)
can.create_window(300,190,window=b1,anchor='nw')

b2 =Button(wind,text='Add Vehicle',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=addvehicle)
can.create_window(300,250,window=b2,anchor='nw')

b3=Button(wind,text='Delete Vehicle',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=delvehicle)
can.create_window(300,310,window=b3,anchor='nw')

b4=Button(wind,text='Display Rented Vehicle',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=rented_vehicle)
can.create_window(300,370,window=b4,anchor='nw')

b5=Button(wind,text='Delete Rented Vehicle',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=delrented)
can.create_window(300,430,window=b5,anchor='nw')

b6=Button(wind,text='Display Rental History',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=rentalhistory)
can.create_window(300,500,window=b6,anchor='nw')

logout=Button(wind,text='Logout',width=8,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='tomato3',foreground='white',command=logout)
can.create_window(610,70,window=logout,anchor='nw')


wind.mainloop()


