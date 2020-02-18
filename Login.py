from selenium import webdriver
import time

# driver1 = webdriver.Chrome(executable_path= "C:\Driver\chromedriver.exe" )
# driver1.get("http://qaweb.corp.hdworks.in/")

def loginfuntion(usern, passwo, driver):
    driver.find_element_by_name("userid").send_keys(usern)
    driver.find_element_by_id("passwordlogindum").click()
    driver.find_element_by_name("password").send_keys(passwo)
    driver.find_element_by_xpath('//*[@id="signin_submit"]').click()
    time.sleep(5)
    adc = driver.find_element_by_xpath('//*[@id="wallet"]/div/input')
    if adc.is_displayed():
        return True
    else:
        print("incorrect login credentials")
        return False
    print(driver.title)
    time.sleep(5)

# driver.minimize_window()


# driver.find_element_by_xpath('//*[@id="refer_btn"]').click()
# driver.find_element_by_xpath("//a[text()='My Rewards']").click()
# driver.find_element_by_xpath('//*[@href="Logout.do"]')