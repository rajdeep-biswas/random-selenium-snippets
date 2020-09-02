# pip install selenium
# find and install browser version specific webdrivers

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Users\\Rajdeep\\Desktop\\chromedriver.exe')

sleep(3)
count = 0

while(1):
    
    driver.get("https://www.w3teaches.com/top-5-two-wheel-electric-scooters")

    sleep(0.5)

    driver.find_element(By.XPATH, '//div[@class="comment-form-textarea ast-col-lg-12"]/textarea[@id="comment"]').send_keys("Nice random comment")
    driver.find_element(By.XPATH, '//p[@class="comment-form-author ast-col-xs-12 ast-col-sm-12 ast-col-md-4 ast-col-lg-4"]/input[@id="author"]').send_keys("Random Name")
    driver.find_element(By.XPATH, '//p[@class="comment-form-email ast-col-xs-12 ast-col-sm-12 ast-col-md-4 ast-col-lg-4"]/input[@id="email"]').send_keys("randomuser@domain.com")
    driver.find_element(By.XPATH, '//p[@class="form-submit"]/input[@name="submit"]').click()    

    print(count)
    count += 1
    
