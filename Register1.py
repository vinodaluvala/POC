from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# driver2 = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
#
# driver2.get("http://qaweb.corp.hdworks.in/")
# driver2.implicitly_wait(3)

def regelements(usera, passw, email,driver):
    try:
        driver.find_element_by_xpath('//input[@id="username"]').send_keys(usera)
        driver.find_element_by_xpath('//input[@id="password"]').send_keys(passw)
        driver.find_element_by_xpath('//input[@id="email"]').send_keys(email)
        driver.find_element_by_xpath('//a[@id="submit_btn"]').click()
        a = driver.find_element(By.XPATH, "//p[@class='text-left']")
        # driver.implicitly_wait(5)
        # driver.find_elements_by_xpath('//a[@href="aboutrummy.html"]').click()
        print(a.text)
        if a.text == 'Thanks for signing up. Your account has been successfully created.':
            print("Registered successfull")
            return True
    except NoSuchElementException:
        print("Incorrect details")
        return False
