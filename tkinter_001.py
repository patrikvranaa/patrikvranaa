import string
from tkinter import *
from turtle import bgcolor, width
from tkcalendar import Calendar, DateEntry
from datetime import *
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

#=========delkarace funkci=========
def getter_data():
     #Vypíše datum
     
     thisDate = cal.get_date()
     print('RadioButton - ' + isRadioButton.get())
     print('CheckButton - ' + isCheckButton.get())
     print('Date - ', thisDate)
     print('SP - ' + hourSpEntry.get())
     print('WZ - ' + hourWZEntry.get())
     print('Other - ' + hourOtherEntry.get())
     print('ComentOther - ' + commentOtherEntry.get())
     print('ComentWT - ' + commentWZEntry.get())
     
def example3():
    #při kliknutí se otevře nové okno
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=thisYear)
    cal.pack(padx=10, pady=10)

#=========delkarace proměných=========
root = tk.Tk()
#Frame - Window setup
frame = Frame(root, padx=5, pady=5)
frame.grid(row=0, column=0)

# nastavi promene casu na aktualní den
today = date.today()
thisDay = int(today.strftime("%d"))
thisMonth = int(today.strftime("%m"))
thisYear = int(today.strftime("%Y"))
# nastaveni promene pro kalendar  - > vyber datumu
cal = DateEntry(frame, width=12, background='#4b0d4c',
                    foreground='white', borderwidth=2, year=thisYear)
#promena pro radioButtons, zazařezní do skupiny
isRadioButton = StringVar() 
isRadioButton.set("1")
#promena pro checkBox, zazařezní do skupiny
isCheckButton = StringVar() 
isCheckButton.set("0")


#=========umístění Wgetu=========

#row=0, column=0
#LabelFrame -> konteiner pro radioButtons
radioButtons = LabelFrame(frame, text='HD:')
radioButtons.grid(row=0, column=0, columnspan=1,sticky='W')
#RadioButtons
rButton1 = ttk.Radiobutton(radioButtons, text="N", variable=isRadioButton, value=0).grid(row=0,column=0)
rButton2 = ttk.Radiobutton(radioButtons, text="1", variable=isRadioButton, value=1).grid(row=0,column=1)
rButton1 = ttk.Radiobutton(radioButtons, text="2", variable=isRadioButton, value=2).grid(row=0,column=2)
rButton2 = ttk.Radiobutton(radioButtons, text="3", variable=isRadioButton, value=3).grid(row=0,column=3)

#row=0, column=0
#LabelFrame -> konteiner pro checkButtons
checkButtons = LabelFrame(frame, text='Porada:')
checkButtons.grid(row=0, column=0, columnspan=1,sticky='E')
#CheckButtons
chButton1 = ttk.Checkbutton(checkButtons, variable=isCheckButton, onvalue=1, offvalue=0).grid(row=0,column=0,sticky='W')


#row=1 column=0
#LabelFrame - konteiner pro datum
# nastaveni promene pro kalendar  - > vyber datumu
datumFrame = LabelFrame(frame, text="Datum")
datumFrame.grid(row=1, column=0, columnspan=1,sticky='W')
cal = DateEntry(datumFrame, width=12, background='#4b0d4c',
                    foreground='white', borderwidth=2, year=thisYear)
#vypsání kalendáře                   
cal.grid(row=1, column=1, padx=10, pady=10,sticky='W')


#row=2 column=0
#LabelFrame - konteiner pro zadávání odpracovaných hodin
hourWored = LabelFrame(frame,text='Hodiny:')
hourWored.grid(row=2, column=0, columnspan=1)
#Lables
hourSPLabel = ttk.Label(hourWored, text='SP').grid(row=2,column=0, padx=10, pady=10)
hourWZLabel = ttk.Label(hourWored, text='WZ').grid(row=3,column=0, padx=10, pady=10)
hourOtherLabel = ttk.Label(hourWored, text='Jiná Práce').grid(row=4,column=0, padx=10, pady=10)
#Entry
hourSpEntry = ttk.Entry(hourWored)
hourSpEntry.grid(row=2,column=1,padx=1,pady=1)
hourWZEntry = ttk.Entry(hourWored)
hourWZEntry.grid(row=3,column=1, padx=5, pady=5)
hourOtherEntry = ttk.Entry(hourWored)
hourOtherEntry.grid(row=4,column=1, padx=5, pady=5)






#row=2 column=1
#LabelFrame - konteiner pro komentar k hodinam hodin
hourComment = LabelFrame(frame,text='Komentař:')
hourComment.grid(row=2, column=1, columnspan=1)
#Lables
hourSPLabel = ttk.Label(hourComment, text='').grid(row=0,column=0, padx=10, pady=10)
hourWZLabel = ttk.Label(hourComment, text='P:').grid(row=1,column=0, padx=10, pady=10)
hourOtherLabel = ttk.Label(hourComment, text='P:').grid(row=2,column=0, padx=10, pady=10)
#Entry
fakeLable = ttk.Label(hourComment)
fakeLable.grid(row=0,column=1, padx=5, pady=5)
commentWZEntry = ttk.Entry(hourComment)
commentWZEntry.grid(row=1,column=1, padx=5, pady=5)
commentOtherEntry = ttk.Entry(hourComment)
commentOtherEntry.grid(row=2,column=1, padx=5, pady=5)



#Buttons
Save = ttk.Button(frame, text='Save', command=getter_data).grid(padx=10, pady=10)




#test code



#Main loop
root.mainloop()