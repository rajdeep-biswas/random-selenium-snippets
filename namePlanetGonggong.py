# pip install selenium
# find and install browser version specific webdrivers

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Users\\Rajdeep\\Desktop\\chromedriver.exe')

sleep(3)
count = 0

while(1):
    
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdttZHfHo9QADrt-OxUQc_MdnU0R9YDum05C7ZR91ohn5NuoA/viewform")

    sleep(0.5)

    driver.find_element(By.XPATH, '//div[@data-value="Gonggong"]//div[@class="quantumWizTogglePaperradioRadioContainer"]/div[@class="quantumWizTogglePaperradioOffRadio exportOuterCircle"]').click()
    driver.find_element(By.XPATH, '//div[@class="quantumWizButtonEl quantumWizButtonPaperbuttonEl quantumWizButtonPaperbuttonFlat quantumWizButtonPaperbuttonDark quantumWizButtonPaperbutton2El2 freebirdFormviewerViewNavigationSubmitButton"]').click()

    print(count)
    count += 1
    
