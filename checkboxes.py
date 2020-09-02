from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import random as rndm
from random import seed
import random
from time import sleep
driver = webdriver.Chrome("C:\\Users\\Rajdeep\\Desktop\\chromedriver.exe")
driver.get("https://www.buzzfeed.com/newsletters")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
