from selenium import webdriver
from xvfbwrapper import Xvfb

vdisplay = Xvfb()
vdisplay.start()

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title

vdisplay.stop()