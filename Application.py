import tkinter as tk

root = tk.Tk()
root.title("Zoom")

start = tk.Button(root, text="Start", command="start")
start.pack()
menu = tk.Button(root, text="Menu", command="menu")
menu.pack()

def start():
    openZoom()
    

root.mainloop()
