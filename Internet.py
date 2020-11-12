from selenium import webdriver
import Programm

def openZoom(program):
    url = program.theRightLink()
    zoom = webdriver.Firefox()
    zoom.get(url)
    
