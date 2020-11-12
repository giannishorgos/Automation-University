from datetime import *
import time

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
                    Program.makeTxtFile(i, lecture, hour, link)
                    lecture.clear()
                    hour.clear()
                    link.clear()
                    
    @staticmethod
    def makeTxtFile(day, lecture, hour, link):
        p = open("{self.username}.txt", "a") 

        for i in range(len(hour)):
            p.write(day + " ")
            p.write(hour[i] + "    ")
            p.write(lecture[i] + "    ")
            p.write(link[i] + "\n")
        p.close()

    def theRightLink(self):
        txtFile = open("/home/giannis/Documents/Codes/Zoom Calls Automation/pl.txt", "r")
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
                if abs(int(line[2:4]) -  hour) <= 1 and abs(int(line[5:7]) - minutes) <= 1:
                    flag = False
                    begins = line.find("https")
                    return line[begins : len(line)]
            time.sleep(30)