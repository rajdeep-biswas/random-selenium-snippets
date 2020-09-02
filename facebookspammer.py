# pip install selenium
# find and install browser version specific webdrivers

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Users\\Rajdeep\\Desktop\\chromedriver.exe')

sleep(3)
count = 1

driver.get("https://www.w3teaches.com/top-5-two-wheel-electric-scooters")
input("log in to your account from the browser window (you might need to enable cookies and then type something and press enter here: ")

while(1):
    
    st = "faggot" + str(count)
    driver.find_element(By.XPATH, '//div[@aria-label="Write a comment..."]').send_keys(st)
    driver.find_element(By.XPATH, '//div[@aria-label="Write a comment..."]').send_keys(Keys.RETURN)     

    count += 1
    
