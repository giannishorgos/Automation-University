from datetime import datetime

def makeTxtFile(day, lecture, hour, link):
    p = open("Program.txt", "a")
    for i in range(len(hour)):
        p.write(day+"    ")
        p.write(lecture[i]+"    ")
        p.write(hour[i]+"    ")
        p.write(link[i]+ "\n")
    p.close()

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
                    makeTxtFile(dic[i], lecture, hour, link)
                    lecture.clear()
                    hour.clear()
                    link.clear()

PRG = Program("username")
PRG.getProgram()