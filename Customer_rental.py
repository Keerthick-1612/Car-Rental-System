from tkinter import *
from PIL  import ImageTk,Image
from tkinter import font
from tkinter import ttk
import time
from datetime import datetime
from Tree import Tree
from tkinter.messagebox import *
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

 



def disvehi(wind3,val,cid,rs,rf):
    def update2():
        wind4.destroy()
        import intro2
    tree=val.get_tree()
    value=tree.item(tree.selection())['values']

    vid=value[0]
    rid=rental_id()
    print(cid,vid,rid)
    #def update1():
    try:
        add_rental(rid,cid,vid,rs,rf)
    except cx_Oracle.DatabaseError:
        showwarning('DATA ERROR','CANNOT RENT A VEHICLE MORE THAN 10 DAYS')
        return  
    wind3.destroy()
    wind4 = Tk() 
    can2=Canvas(wind4,bg='white',width=710,height=300)
    can2.pack()
    # upd_button=Button(wind4,text='Add',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
    #                     background='DodgerBlue3',foreground='white',command=update1)
    # back_button=Button(wind4,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
    #                     background='DodgerBlue3',foreground='white',command=lambda: can2.destroy())
    # can2.create_window(300,20,window=upd_button,anchor='nw')
    # can2.create_window(300,250,window=back_button,anchor='nw')
    can2.create_text(350,70,text='Bill',anchor='nw',font=font.Font(family='Ailza Bright Demo',underline=1,size=17,weight='bold'),fill='Dodgerblue4')
    record=bill(cid,vid,rid)
    print(record)
    if len(record)>2:
        tree1=Tree(wind4,1,6)
    else:
        
        tree1=Tree(wind4,len(record),6)
    
    tree1.create_headings(['FirstName','LastName', 'RentalDate', 'ReturnDate','Unit Price',"Total"])
    tree1.add_data(record)
    can2.create_window(30,100,anchor='nw',window=tree1.get_tree())
    b1 =Button(wind4,text='Logout',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=update2)
    can2.create_window(300,250,window=b1,anchor='nw')
    
    wind4.mainloop()


def next(cid):


    wind.destroy()
    wind3=Tk()
    wind3.geometry(f'600x349+{280}+{50}')
    wind3.resizable(False,False)
    wind3.iconbitmap('icon.ico')
    can3=Canvas(wind3,width=600,height=349)
    can3.pack()
   
    
    req_list=display_vehicle()

    if len(req_list)+1>5:
        tree=Tree(wind3,5,5)
    else:
        
        tree=Tree(wind3,len(req_list)+1,5)
    
    tree.create_headings(['VehicleID', 'Model', 'Make', 'Year', 'RentalRate'])
    tree.add_datas(req_list)
    can3.create_text(180,70,text='Available Vehicles',anchor='nw',font=font.Font(family='Ailza Bright Demo',underline=1,size=17,weight='bold'),fill='Dodgerblue4')
    can3.create_window(35,100,anchor='nw',window=tree.get_tree())
    rentalstart=Entry(wind3,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    rentalfinish=Entry(wind3,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    rentalstart.insert(0,'YYYY-MM-DD')
    rentalfinish.insert(0,'YYYY-MM-DD')
    rentalstart.bind('<Button-1>',lambda e: rentalstart.delete(0,END))
    rentalfinish.bind('<Button-1>',lambda e: rentalfinish.delete(0,END))
    can3.create_text(30,22,text='RentalDate',anchor='nw',font=font.Font(family='Ailza Bright Demo',underline=1,size=17,weight='bold'),fill='Dodgerblue4')
    can3.create_text(300,22,text='ReturnDate',anchor='nw',font=font.Font(family='Ailza Bright Demo',underline=1,size=17,weight='bold'),fill='Dodgerblue4')
    can3.create_window(175,22,window=rentalstart,anchor='nw')
    can3.create_window(450,22,window=rentalfinish,anchor='nw')
    b1 =Button(wind3,text='Add For Rent',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda : disvehi(wind3,tree,cid,rentalstart.get(),rentalfinish.get()))
    can3.create_window(300,250,window=b1,anchor='nw')
    wind3.mainloop()


def addcustomer():
    cid=cust_id()
    def update1():
        add_customer(cid,fname.get(),lname.get(),email.get(),phone.get(),address.get())
    #'VehicleID', 'Model', 'Make', 'Year', 'RentalRate'
    can2=Canvas(wind,bg='white',width=460,height=300)
    can.create_window(150,60,window=can2,anchor='nw')
    can2.create_text(120,90,text='First Name ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,130,text='Last Name ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,170,text='Email ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,210,text='Phone ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,250,text='Address ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')

    fname=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    lname=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    email=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    phone=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    address=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    upd_button=Button(wind,text='Add',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=update1)
    back_button=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=lambda: can2.destroy())
    
    # item.insert(0,data[1])
    # quty.insert(0,data[2])
    # cost.insert(0,data[-1])
    
    can2.create_window(200,70,window=fname,anchor='nw')
    can2.create_window(200,110,window=lname,anchor='nw')
    can2.create_window(200,150,window=email,anchor='nw')
    can2.create_window(200,190,window=phone,anchor='nw')
    can2.create_window(200,230,window=address,anchor='nw')
    can2.create_window(300,20,window=upd_button,anchor='nw')
    can2.create_window(300,250,window=back_button,anchor='nw')
    b3 =Button(wind,text='Next',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command= lambda : next(cid))
    can.create_window(300,350,window=b3,anchor='nw')
def prevcustomer():
    cid=None
    def update1():
        global cid
        cid=identify_cust(fname.get(),lname.get())
        print(cid)
        if cid is None:
            showwarning('DATA ERROR','CID NOT FOUND FOR GIVE FIRST AND LAST NAME')
        else:
            next2=Button(wind,text='Next',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                            background='DodgerBlue3',foreground='white',command= lambda : next(cid))
            can2.create_window(100,250,window=next2,anchor='nw')


    can2=Canvas(wind,bg='white',width=460,height=300)
    can.create_window(150,60,window=can2,anchor='nw')
    can2.create_text(120,90,text='First Name ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    can2.create_text(120,130,text='Last Name ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
    fname=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    lname=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    can2.create_window(200,70,window=fname,anchor='nw')
    can2.create_window(200,110,window=lname,anchor='nw')
    print(fname.get(),lname.get())
    check=Button(wind,text='Check',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=update1 )
    back_button=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                        background='DodgerBlue3',foreground='white',command=lambda: can2.destroy())

    can2.create_window(300,20,window=check,anchor='nw')
    can2.create_window(300,250,window=back_button,anchor='nw')
# def display_customer():
#     def update3(): 
#             req_list=display_cust_given()

#             if len(req_list)+1>5:
#                 tree=Tree(wind3,5,5)
#             else:
                
#                 tree=Tree(wind3,len(req_list)+1,5)
            
#             tree.create_headings(['VehicleID', 'Model', 'Make', 'Year', 'RentalRate'])
#             tree.add_datas(req_list)

#     can2=Canvas(wind,bg='white',width=460,height=300)
#     can.create_window(150,60,window=can2,anchor='nw')
#     can2.create_text(120,90,text='First Name ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
#     can2.create_text(120,130,text='Last Name ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
#     fname=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
#     lname=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
#     can2.create_window(200,70,window=fname,anchor='nw')
#     can2.create_window(200,110,window=lname,anchor='nw')
#     check=Button(wind,text='Check',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
#                         background='DodgerBlue3',foreground='white',command=update3 )
#     can2.create_window(300,20,window=check,anchor='nw')


b9 =Button(wind,text='Old Customer',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=prevcustomer)
can.create_window(300,200,window=b9,anchor='nw')


b2 =Button(wind,text='New Customer',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=addcustomer)
can.create_window(300,300,window=b2,anchor='nw')

# b8=Button(wind,text='New Customer',width=20,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=dis_customer)
# can.create_window(300,300,window=b2,anchor='nw')
wind.mainloop()



