from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_service=Service("C:\Chrome-Driver\chromedriver.exe")
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

data=driver.find_element(By.CSS_SELECTOR, '#articlecount a')
#data=driver.find_element(By.CSS_SELECTOR, "#articlecount a" - this will give the first value of a
# print(data.text)

# CLICK ON BUTTON FUNCTION
# data.click()

# CLICK ON LINK TEXT ABILITY - ALLOWS TO CLICK ON A PARTICULAR LINK TEXT YOU'RE INTERESTED IN
all_portals=driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# SEARCH FUNCTION
search=driver.find_element(By.NAME, "search")
search.send_keys("Python")
# ACTIVATE THE ENTER BUTTON
search.send_keys(Keys.ENTER)