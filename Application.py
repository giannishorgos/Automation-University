import tkinter as tk
from Internet import openZoom
from selenium import webdriver
from Programm import Program


day = 0
hour = []
lecture = []
link = []

def get(entryLecture, entryHour, entryLink): #tha baleis kai ta labels
    lecture.append(entryLecture.get())
    hour.append(entryHour.get())
    link.append(entryLink.get())
    program.makeTxtFile(day, lecture, hour, link)
    lecture.clear()
    hour.clear()
    link.clear()
    getProgram()
    # entryLecture.pack_forget() .. etc

def yes():

    dic = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
    lableDay = tk.Label(root, text=dic[day])
    lableDay.pack()

    lableLecture = tk.Label(root, text="Gimme Lecture")
    lableLecture.pack() #auto se ola
    entryLecture = tk.Entry(root)
    entryLecture.pack()
    
    lableHour = tk.Label(root, text="Begins at:").pack()
    entryHour = tk.Entry(root)
    entryHour.pack()
    
    lableLink = tk.Label(root, text="The link for the call is:").pack()
    entryLink= tk.Entry(root)
    entryLink.pack()
    
    btnNext = tk.Button(root, text="Next", command=lambda : get(entryLecture, entryHour, entryLink))
    btnNext.pack()

def no():
    global day
    day += 1
    if day < 5:
        getProgram()

def start():
    openZoom(program)
    #mia while edw prepei

def menu():
    #program.getProgram()
    labelUsername  = tk.Label(root, text='Username').pack()
    entryUsername = tk.Entry(root)
    entryUsername.pack()
    buttonOk = tk.Button(root, text="OK", command=lambda : getUsername(entryUsername))
    buttonOk.pack()

    buttonGetProgram = tk.Button(root,text="Gimme program", command=getProgram)
    buttonGetProgram.pack()

def getProgram():
    labelchoice = tk.Label(root, text="Do you want to add something?").pack()
    buttonYes = tk.Button(root, text="Yes", command=yes).pack()
    buttonNo = tk.Button(root, text="No", command=no).pack()

def getUsername(entryUsername):
    print(entryUsername.get())
    program.setUsername(entryUsername.get())
    entryUsername.pack_forget()



#Game-Loop
root = tk.Tk()
root.title("Zoom")
program = Program()
start = tk.Button(root, text="Start", command=start)
menu = tk.Button(root, text="Menu", command=menu)
start.pack()
menu.pack()

root.mainloop()

    

