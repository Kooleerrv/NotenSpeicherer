import tkinter as tk
import json
import matplotlib.pyplot as plt

 


# read file
with open("Notenn.json", "r") as myfile:
    data=myfile.read()

# parse file
General = json.loads(data)

# show values
#print(General)
Fach = ""


#Result=0
root = tk.Tk()
root.config(height=700,width=1244, bg="#282828")

frame=tk.Frame(root, bg="#282828")
frame.place(relwidth=0.5, relheight=0.647, relx=0, rely=0)


Result=0

def write_json(data, filename="Notenn.json"): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 




def sPhysik():
    global Fach
    Fach="Physik"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)
   
def sDeutsch():
    global Fach
    Fach="Deutsch"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)
    
def sFrench():
    global Fach
    Fach="Franz"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)
    
def sGG():
    global Fach
    Fach="GG"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)
    
def sMathe():
    global Fach
    Fach="Mathe"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)    

def sMusik():
    global Fach
    Fach="Musik"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)
    
def sBG():
    global Fach
    Fach="BG"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)
    
def sTurnen():
    global Fach
    Fach="BuS"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)

def sGS():
    global Fach
    Fach="GS"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)       

def sEnglisch():
    global Fach
    Fach="Englisch"
    Notenauslesehr()
    Schnitt = tk.Label(frame, text= Result, fg="white", bg="#404040")
    Schnitt.config(height=2,width=16)
    Schnitt.grid(column=2,row=1)

    
def Notenauslesehr():
    notecount=0
    notesum=0
    global Result
    Result=""
    for each in General["Noten"]:
        #check if a line with the "Fach" "Deutsch" exists
        if each["Fach"] == Fach:
            found = True
            #then append a line with "Note", "Datum", "Thema"
            for any in each["NotenDatumThema"]:
                note = float(any["Note"])
                notecount = notecount + 1;
                notesum = notesum + note;
    
    if notecount > 0:
        Result = str(notesum / notecount)
    else:  
        Result = None
    
def graph():
    x=[]
    y=[]

    with open('Notenn.json','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))

    plt.plot(x,y, label='Loaded from file!')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()
    
    
def neue_Note():
    global newWindow
    newWindow=tk.Toplevel()
    newWindow.config(bg="#282828")



    Fachl = tk.Label(newWindow, text="Fach",bg="#282828", fg="white")
    Fachl.grid(column=0,row=0)

    global Fach
    Fach = tk.StringVar()
    Fach.set("Bitte Auswählen")
    Fachmenu = tk.OptionMenu(newWindow, Fach, "Physik", "Deutsch", "Franz", "GG","Mathe", "Musik", "BG", "BuS", "GS", "Englisch")
    Fachmenu.config(width=14,bg="#282828", fg="white")
    Fachmenu.grid(column=1,row=0)



    Note= tk.Label(newWindow, text="Note: ",bg="#282828", fg="white")
    Note.grid(column=0, row=1)
    
    global Notee
    Noteestr=""
    Notee = tk.Entry(newWindow, textvariable=Noteestr,bg="#282828", fg="white")
    Notee.grid(column=1, row=1)



    DatumL = tk.Label(newWindow, text="Datum: (TT/MM)",bg="#282828", fg="white")
    DatumL.grid(column=0,row=4)

    global Datum
    global Datumstr
    Datumstr = ""
    Datum = tk.Entry(newWindow, textvariable=Datumstr,bg="#282828", fg="white")
    Datum.grid(column=1,row=4)


    global Thema
    Themastr = ""
    Thema = tk.Entry(newWindow, textvariable=Themastr,bg="#282828", fg = "white")
    Thema.grid(column=1, row= 5)

    ThemaL = tk.Label(newWindow, text="Thema:", bg="#282828", fg="white")
    ThemaL.grid(column=0, row=5)

    
    Button=tk.Button(newWindow, text="Finished", command=Finished, bg="#282828", fg="white")
    Button.grid(column=0,row=6)


    
        
def Finished():

    #Get data from Entry/Drop down Menu
    Fachstr= Fach.get()
    Datumstr = Datum.get()
    Noteestr =  Notee.get()
    Themastr = Thema.get()
    
    FachundNote = Fachstr+"/"+Noteestr+"\n"
    print(Fachstr)
    print(Noteestr)
    print(Datumstr)
    print(Themastr)

    # read file
    with open("Notenn.json", "r") as myfile:
        data=myfile.read()

    # parse file
    General = json.loads(data)

    # show values

    found = False

    for each in General["Noten"]:
        #check if a line with the same "Fach" exists
        if each["Fach"] == Fachstr:
            found = True
            #then append a line with "Note", "Datum", "Thema"
            each["NotenDatumThema"].append({
                'Note': Noteestr,
                'Datum': Datumstr,
                'Thema': Themastr
            })

    # if no record found then create a new entry
    if found == False:
        General["Noten"].append({
            'Fach': Fachstr,
            'NotenDatumThema': [{
                'Note': Noteestr,
                'Datum': Datumstr,
                'Thema': Themastr
            }]
        })
  
  
    # appending data to emp_details  
    #temp.append(y) 
      
    write_json(General)  

    newWindow.withdraw()



        
 

  




newGrade= tk.Button(frame, text="neue Note", fg="white", bg="#404040", command=neue_Note)
newGrade.config(height=2,width=16)
newGrade.grid(column=0, row=11)




Physik = tk.Button(frame, text="Physik", fg="white", bg="#404040", command=sPhysik)
Physik.config(height=2,width=16)
Physik.grid(column=0, row=1)

Deutsch = tk.Button(frame, text="Deutsch", fg="white", bg="#404040", command=sDeutsch)
Deutsch.config(height=2,width=16)
Deutsch.grid(column=0, row=2)

French = tk.Button(frame, text="French", fg="white", bg="#404040", command=sFrench)
French.config(height=2,width=16)
French.grid(column=0, row=3)

GG = tk.Button(frame, text="GG", fg="white", bg="#404040", command= sGG)
GG.config(height=2,width=16)
GG.grid(column=0,row=4)

Mathe = tk.Button(frame, text="Mathe", fg="white", bg="#404040", command= sMathe)
Mathe.config(height=2,width=16)
Mathe.grid(column=0,row=5)

Musik = tk.Button(frame, text="Musik", fg="white", bg="#404040", command = sMusik)
Musik.config(height=2,width=16)
Musik.grid(column=0,row=6)

BG = tk.Button(frame, text="BG", fg="white", bg="#404040", command = sBG)
BG.config(height=2,width=16)
BG.grid(column=0,row=7)

Turnen = tk.Button(frame, text="Turnen", fg="white", bg="#404040", command = sTurnen)
Turnen.config(height=2,width=16)
Turnen.grid(column=0,row=8)

GS = tk.Button(frame, text="GS", fg="white", bg="#404040", command= sGS)
GS.config(height=2,width=16)
GS.grid(column=0,row=9)

Englisch = tk.Button(frame, text="Englisch", fg="white", bg="#404040", command = sEnglisch)
Englisch.config(height=2,width=16)
Englisch.grid(column=0,row=10)

root.mainloop()
