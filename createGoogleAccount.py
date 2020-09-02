# pip install selenium
# find and install browser version specific webdrivers

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path='path\\to\\chromedriver.exe')

sleep(12)

driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")

sleep(3)

elem = driver.find_element_by_name("firstName")
elem.send_keys("userZa78sdy6xcno")

elem = driver.find_element_by_name("lastName")
elem.send_keys("userKnt1i102389ey")

elem = driver.find_element_by_name("Username")
elem.send_keys("emaildy6x1i10cnox")

elem = driver.find_element_by_name("Passwd")
elem.send_keys("mofos1234")

elem = driver.find_element_by_name("ConfirmPasswd")
elem.send_keys("mofos1234")

elem = driver.find_element_by_id("accountDetailsNext")
elem.send_keys(Keys.RETURN)
