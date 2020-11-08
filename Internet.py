from selenium import webdriver

zoom = webdriver.Firefox()

program = Program("user")

def openZoom():
    zoom.get(program.theRightLink())
    
