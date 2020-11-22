from selenium import webdriver
import Programm

def openZoom(program):
    url = program.theRightLink()
    if url != "":
        zoom = webdriver.Firefox()
        zoom.get(url)
    else:
        print('today you are FREE')
    
