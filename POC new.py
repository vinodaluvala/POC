from selenium import webdriver
from Login import loginfuntion
from Register1 import regelements
from Addcash import addCash

import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

driver.get("http://qaweb.corp.hdworks.in/")
driver.implicitly_wait(3)
driver.maximize_window()
print("Title of the page:", driver.title)

#Test Case 1(Login and Add cash)
userName="godofwar"
password="ace2three"
#Passing the same 'driver' as the parameter to maintain one instance

loginfuntion(userName, password, driver)        #Calling function from Login.py module
time.sleep(5)
addCash(driver)
driver.find_element_by_xpath('//*[@href="Logout.do"]').click()
time.sleep(2)

#Test Case 2(Signup new user)
driver.get("http://qaweb.corp.hdworks.in/")
regUserName = "corsivi"          #Please enter new username
regPassword = "cororades"        # Please enter password
regEmail = "corossores@123.com"  # Please enter email name everytime

if regelements(regUserName, regPassword, regEmail, driver):     #calling function from Register1.py Module
    print("Singed up with "+regUserName+" Successfully")
    driver.find_element_by_xpath('//*[@href="Logout.do"]').click()
    print("Logged out "+regUserName+" successfully")
else :
    print ("Signup Failed...Try again Later")

driver.close()


# driver.find_element_by_xpath("//a[text()='My Rewards']").click()
# driver.find_element_by_xpath('//*[@id="refer_btn"]').click()
