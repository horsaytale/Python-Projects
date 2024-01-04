from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_service=Service("C:\Chrome-Driver\chromedriver.exe")
driver=webdriver.Chrome(service=chrome_service)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name=driver.find_element(By.NAME,"fName")
f_name.send_keys("Lydia")

l_name=driver.find_element(By.NAME,"lName")
l_name.send_keys("Troiv")

email=driver.find_element(By.NAME,"email")
email.send_keys("lydia@hotmail.com")

sign_up=driver.find_element(By.CLASS_NAME,"btn")
sign_up.click()
#ANOTHER METHOD
# sign_up.send_keys(Keys.ENTER)