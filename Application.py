import tkinter as tk
from Internet import openZoom
from selenium import webdriver

root = tk.Tk()
root.title("Zoom")
program = Program("user")

start = tk.Button(root, text="Start", command="start")
start.pack()
menu = tk.Button(root, text="Menu", command="menu")
menu.pack()

def start():
    openZoom(program)

def menu():
    program.getProgram()


def openZoom(program):
    url = program.theRightLink()
    zoom = webdriver.Firefox()
    zoom.get(url)
    

root.mainloop()
