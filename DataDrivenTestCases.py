import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import XLUtilites

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/login")
driver.maximize_window()

path = "C://SeleniumPractice/LoginTest.xlsx"

rows = XLUtilites.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username = XLUtilites.readData(path, "Sheet1",r,1)
    password = XLUtilites.readData(path, "Sheet1",r,2)

    driver.find_element(By.ID, 'email').send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, '//button[@id="login"]').click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//img[contains(@class,'zl-navbar-rhs-img ')]").click()
    driver.find_element(By.XPATH,  "//a[contains(.,'Logout')]").click()
    time.sleep(10)

    if driver.title == "Home Page":
      print("Test is Passed")
      XLUtilites.writeData(path, "Sheet1",r,3,"Passed")
    else:
      print("Test is Failed")
      XLUtilites.writeData(path, "Sheet1",r,3,"Failed")

    driver.find_element(By.XPATH,"//a[contains(text(),'Sign In')]").click()
    time.sleep(5)