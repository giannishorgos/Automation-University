import tkinter as tk
from Internet import openZoom
from selenium import webdriver
from Programm import Program


day = 0
hour = []
lecture = []
link = []

def get(entryLecture, entryHour, entryLink, labelLecture, labelHour, labelLink, labelDay, btnNext): #tha baleis kai ta labels
    lecture.append(entryLecture.get())
    hour.append(entryHour.get())
    link.append(entryLink.get())
    program.makeTxtFile(day, lecture, hour, link)

    lecture.clear()
    hour.clear()
    link.clear()

    entryLecture.pack_forget()
    entryHour.pack_forget()
    entryLink.pack_forget()
    labelLecture.pack_forget()
    labelHour.pack_forget()
    labelLink.pack_forget()
    btnNext.pack_forget()
    labelDay.pack_forget()

    getProgram()
    

def yes(labelChoice, buttonYes, buttonNo):
    labelChoice.pack_forget()
    buttonYes.pack_forget()
    buttonNo.pack_forget()

    dic = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
    labelDay = tk.Label(root, text=dic[day])
    labelDay.pack()

    lableLecture = tk.Label(root, text="Gimme Lecture")
    lableLecture.pack() #auto se ola
    entryLecture = tk.Entry(root)
    entryLecture.pack()
    
    lableHour = tk.Label(root, text="Begins at:")
    lableHour.pack()
    entryHour = tk.Entry(root)
    entryHour.pack()
    
    lableLink = tk.Label(root, text="The link for the call is:")
    lableLink.pack()
    entryLink= tk.Entry(root)
    entryLink.pack()
    
    btnNext = tk.Button(root, text="Next", command=lambda : get(entryLecture, entryHour, entryLink, lableLecture, lableHour, lableLink, labelDay, btnNext))
    btnNext.pack()

def no(labelchoice, buttonNo, buttonYes):
    labelchoice.pack_forget()
    buttonNo.pack_forget()
    buttonYes.pack_forget()

    global day
    day += 1
    if day < 5:
        getProgram()

def start(start_, menu_):
    start_.pack_forget()
    menu_.pack_forget()

    labelUsername  = tk.Label(root, text='Username')
    labelUsername.pack()
    entryUsername = tk.Entry(root)
    entryUsername.pack()
    buttonOk = tk.Button(root, text="OK", command=lambda : getUsername(entryUsername, buttonOk, labelUsername))
    buttonOk.pack()

    
    #mia while edw prepei

def menu(start_, menu_):
    #program.getProgram()
    start_.pack_forget()
    menu_.pack_forget()

    labelUsername  = tk.Label(root, text='Username')
    labelUsername.pack()
    entryUsername = tk.Entry(root)
    entryUsername.pack()
    buttonOk = tk.Button(root, text="OK", command=lambda : getUsername(entryUsername, buttonOk, labelUsername, buttonGetProgram))
    buttonOk.pack()

    buttonGetProgram = tk.Button(root,text="Gimme program", command=getProgram)

def getProgram():
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
    labelChoice = tk.Label(root, text="Do you want to add something? (" + days[day] + ")")
    labelChoice.pack()
    buttonYes = tk.Button(root, text="Yes", command=lambda : yes(labelChoice, buttonYes, buttonNo))
    buttonYes.pack()
    buttonNo = tk.Button(root, text="No", command= lambda : no(labelChoice, buttonNo, buttonYes))
    buttonNo.pack()

def getUsername(entryUsername, buttonOk, labelUsername, buttonGetProgram=None):
    print(entryUsername.get())
    program.setUsername(entryUsername.get())

    entryUsername.pack_forget()
    buttonOk.pack_forget()
    labelUsername.pack_forget()
    if buttonGetProgram != None:
        buttonGetProgram.pack()
    else:
        openZoom(program)



#Game-Loop
root = tk.Tk()
w = tk.Canvas(root, width=200, height=200)
root.title("Zoom")
program = Program()
start_ = tk.Button(root, text="Start", command=lambda : start(start_, menu_))
menu_ = tk.Button(root, text="Menu", command=lambda : menu(start_, menu_))
start_.pack()
menu_.pack()
w.pack()

root.mainloop()

    

