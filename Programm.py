from datetime import *
import time
import os

class Program:
    def __init__(self, username):
        self.username = username

    def getProgram(self):
        #mera, wra, mathhma kai link
        hour = []
        lecture = []
        link = []

        dic = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

        for i in range(5):
            flag = True
            print(dic[i])
            while flag:     
                choice = str(input("Do you want to add something? [Y/N]"))
                if choice == 'N' or choice == 'n':
                    flag = False
                else:
                    lecture.append(str(input("LECTURE: ")))
                    hour.append(str(input("Begins at: ")))
                    link.append(str(input("The link for the call is: ")))
                    self.makeTxtFile(i, lecture, hour, link)
                    lecture.clear()
                    hour.clear()
                    link.clear()
                    
    def makeTxtFile(self, day, lecture, hour, link):
        currentDir = os.getcwd()
        p = open(currentDir + "/" + self.username + ".txt", "a") 

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
                txtFile = open("/home/giannis/Documents/Codes/Zoom Calls Automation/pl.txt", "r")
                line = txtFile.readline()
            
            if int(line[0]) == day:
                if abs(int(line[2:4]) -  hour) <= 1 and abs(int(line[5:7]) - minutes) <= 20:
                    flag = False
                    begins = line.find("https")
                    return line[begins : len(line)]
