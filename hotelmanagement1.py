
import tkinter 
from tkinter import * 
import datetime as dt
from tkinter import messagebox
#from tkinter.ttk import *
from time import strftime
import sqlite3

con= sqlite3.connect("details.db")
cur=con.cursor()
cur.execute(" " " CREATE TABLE IF NOT EXISTS hotelmanagement(customerid integer PRIMARY KEY AUTOINCREMENT,table_no integer,menu text,totalbillgenerated int,date text,time text);" " ")

def add_new_bill():
    newUserId=customerid_entry.get()
    newTableId=tableid_entry.get()
    newMenu=label.get(1.0,"end-1c")
    newTotalBill=lbl_total.get()
    newDate=label1.cget("text")
    newTime=labelclock.cget("text")
    cur.execute("SELECT COUNT(*) from hotelmanagement WHERE customerid=' "+newUserId+"'")
    result=cur.fetchone()
    

    if int(result[0]) > 0:
        messagebox.showerror("customer id already exists")
    else:
        
        cur.execute("INSERT INTO hotelmanagement(customerid,table_no,menu,totalbillgenerated,date,time) VALUES(?,?,?,?,?,?)",(newUserId,newTableId,newMenu,newTotalBill,newDate,newTime))
        con.commit()
        messagebox.showinfo("added data successfully")

def view_row():
    
   cur.execute("SELECT * FROM hotelmanagement")
   v=cur.fetchall()
   print(v)


window = tkinter.Tk()
def time():
    string = strftime('%H:%M:%S %p')
    labelclock.config(text=string)
    labelclock.after(1000, time)
 
  
window.geometry("800x600")    
date=dt.datetime.now()
window.title("Hotel Management system")

def displaySelected(menu):
    choice=menu.split(":")
    label.insert(END,"{} {}\n".format(choice[0],choice[1]))
    c=choice[1].split()
    
    global total    
    total=total+int(c[1])
    #print(total)


def displaySelectedPayment(payment):
    choice1=payment.split(":")
    label.insert(END," {}\n".format(choice1[0]))
    
def totalbill():
    lbl_total.insert(0,"rs {}/-".format(total))


#frame 1
frame1=Frame(window,bg="red",highlightbackground="black",width=300,height=370)
frame1.place(x=0,y=0)

menu=StringVar()
menu.set("Menu")
items=["Tea: rs 10", "Coffee: rs 20","Paneer tikka: rs 180","Chole bhature: rs 180","Biryani: rs 120","Roti: rs 10","Pav bhaji: rs 100"]
dropdown= OptionMenu(frame1, menu,*items,command=displaySelected)  
dropdown.config(width=8,font=("calibri",15))
dropdown.place(x=5,y=5)

#frame 2
frame2=Frame(window,bg="green",width=300,height=370)
frame2.place(x=0,y=370)
table=StringVar() 
lbl_table=Label(frame2,font=("calibri",15),text="Table",bg="lightgrey",relief=SUNKEN)
lbl_table.place(x=5,y=52)

table_entry=Entry(frame2,font=("calibri",15),textvariable=table,bg="lightgrey",bd=3,width=10)
table_entry.place(x=75,y=50)

view_button=Button(frame2,text="View",bd=5,font=("calibri",15),width=4,command=view_row)
view_button.place(x=3,y=100)


#frame 3
frame3=Frame(window,bg="blue",width=740,height=740)
frame3.place(x=300,y=0)
total=0
label=Text(frame3,bg="white",width=55,height=18)
label.place(x=20,y=150)

tableid=StringVar()
lbl_tableid= Label(frame3,font=("calibri",15),text="Table ID",bg="lightgrey",relief=SUNKEN,width=12)
lbl_tableid.place(x=20,y=60)

tableid_entry=Entry(frame3,font=("calibri",15),textvariable=tableid,bg="lightgrey",bd=3,width=20)
tableid_entry.place(x=160,y=58)

customerid=StringVar()
lbl_customerid=Label(frame3,font=("calibri",15),text="Customer ID",bg="lightgrey",relief=SUNKEN,width=12)
lbl_customerid.place(x=20,y=15)

customerid_entry=Entry(frame3,font=("calibri",15),textvariable=customerid,bg="lightgrey",bd=3,width=20)
customerid_entry.place(x=160,y=15)


label1 = Label(frame3, text=f"{date:%A, %B %d, %Y}", font="Calibri, 15")
label1.place(x=20,y=105)
labelclock= Label(window,  font="Calibri, 15")
labelclock.place(x=600,y=105)
time()

payment=StringVar()
payment.set("Payment Mode")
paymentmode=["cash:","card:","paytm/upi:"]
dropdown1= OptionMenu(frame3, payment,*paymentmode,command= displaySelectedPayment)  
dropdown1.config(width=12,font=("calibri",15))
dropdown1.place(x=330,y=450)

b2=Button(frame3,text="Total",bd=5,font=("calibri",15),width=4,height=0,command=totalbill)
b2.place(x=3,y=450)

add_button=Button(frame3,text="Add",bd=5,font=("calibri",15),width=4,command=add_new_bill)
add_button.place(x=3,y=510)

close_button=Button(frame3,text="Close",bd=5,font=("calibri",15),width=4,command=window.destroy)
close_button.place(x=330,y=500)



total=0
lbl_total=Entry(frame3,font=("calibri",15),bg="lightgrey",relief=SUNKEN,width=12)
lbl_total.place(x=70,y=450)

window.mainloop()


  

