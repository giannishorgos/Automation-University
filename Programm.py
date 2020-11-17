from datetime import *
import time
import os

class Program:
    def __init__(self, username=None):
        self.username = username
    
    def setUsername(self, username):
        self.username = username
                    
    def makeTxtFile(self, day, lecture, hour, link):
        currentDir = os.getcwd()
        windows = "\\"
        linux = "/"
        if linux in currentDir:
            p = open(currentDir + linux + self.username + ".txt", "a") 
        else:
            p = open(currentDir + windows + self.username + ".txt", "a")

        for i in range(len(hour)):
            p.write(str(day) + " ")
            p.write(hour[i] + " ")
            p.write(lecture[i] + " ")
            p.write(link[i] + "\n")
        p.close()

    def theRightLink(self):
        currentDir = os.getcwd()
        txtFile = open(currentDir + "/" + self.username + ".txt", "r")
        flag = True

        i = 0
        while flag: #trexei synexeia auth
            day = datetime.today().weekday()
            hour = datetime.now().hour
            minutes = datetime.now().minute
            line = txtFile.readline()
            if len(line) == 0:
                txtFile.close()
                txtFile = open(currentDir + "/" + self.username + ".txt", "r")
                line = txtFile.readline()
            
            if int(line[0]) == day:
                thour = (int(line[2:4]) -  hour)*60
                tminutes =  int(line[5:7]) - minutes + thour
                if tminutes <= 30 and abs((int(line[2:4]) -  hour)) <= 1:
                    flag = False
                    begins = line.find("https")
                    return line[begins : len(line)]
