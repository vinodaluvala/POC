from selenium import webdriver

import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# driver3 = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
#
# driver3.get("http://qaweb.corp.hdworks.in/")
# driver3.implicitly_wait(3)
# //*[@id='welcomeAddcash']
def addCash(driver):
    driver.find_element_by_xpath('//input[@value="Add Cash"]').click()
    driver.find_element_by_xpath('//input[@id="p_custom_amount"]').clear()
    driver.find_element_by_xpath('//input[@id="p_custom_amount"]').send_keys("200")
    driver.find_element_by_xpath('//*[@id="wallets"]').click()
    driver.find_element_by_xpath('//*[@id="parentVerticalTab"]/div[1]/div[5]/div/div[2]/table/tbody/tr[1]/td[4]/img').click()
    firstWindow = driver.window_handles[0]
    driver.find_element_by_xpath('//*[@id="PayButtonId"]/div[2]/a').click()
    secondWindow = driver.window_handles[1]
    driver.implicitly_wait(2)
    driver.switch_to.window(secondWindow)
    driver.find_element_by_xpath('//input[@value="Mobikiwik PAY"]').click()
    driver.switch_to.window(firstWindow)
    succeMsg= driver.find_element_by_class_name('msgcontent_new')
    print("added cash info" +succeMsg.text)
    addedCash= [int(i) for i in succeMsg.text.split() if i.isdigit()]
    print("successfully added cash :" + str(addedCash[0]))
