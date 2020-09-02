from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome("C:\\Users\\Rajdeep\\Desktop\\chromedriver.exe")
driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
actions = ActionChains(driver)
sleep(5)
actions.move_by_offset(95, 317).click().perform()
