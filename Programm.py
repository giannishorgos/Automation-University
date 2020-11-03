from datetime import datetime

def makeTxtFile(day, lecture, hour, link):
    pass

class Program:
    def __init__(self, username):
        self.username = username

    def getProgram(self):
        #mera, wra, mathhma kai link
        day = ''
        hour = []
        lecture = []
        link = []

        dic = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

        for i in range(5):
            flag = True
            print(dic[i])
            while flag:      
                choice = str(input("Do you want to add something? [Y/N]"))
                if choice == 'Y' or choice == 'y':
                    flag = False
                else:
                    lecture.append(str(input("LECTURE: ")))
                    hour.append(str(input("Begins at: ")))
                    link.append(str(input("The link for the call is: ")))

            makeTxtFile(dic[i], lecture, hour, link)