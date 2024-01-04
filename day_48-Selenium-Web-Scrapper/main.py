from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path=r"C:\Chrome-Driver\chromedriver.exe"
chrome_service=Service(executable_path=chrome_driver_path)

driver=webdriver.Chrome(service=chrome_service)

#driver.get("https://www.amazon.com/Bluetooth-Headphones-Wireless-Memory-Protein-Earmuffs/dp/B08MJV4X7R/ref=sr_1_2_sspa?crid=3F0HU0G5MYLGO&keywords=headphones&qid=1643777876&sprefix=headphone%2Caps%2C405&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTU5BMjU0QUZKMzNKJmVuY3J5cHRlZElkPUEwNTgxNzAxWUJTTEVMOU5LWFI4JmVuY3J5cHRlZEFkSWQ9QTAwMzA1NjgzVjhUODYzWkhZVVo5JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1")
# price=driver.find_element_by_class_name('apexPriceToPay')
# print(price.text)


driver.get("https://www.python.org/")
search_bar=driver.find_element(By.NAME,"q")
#this shows the type of this element [searchbar]
print(search_bar.tag_name)
#this allows you to track what value does the placeholder attr holds
print(search_bar.get_attribute("placeholder"))

logo=driver.find_element(By.CLASS_NAME,"python-logo")
print(logo.size)

doc_link=driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
print(doc_link.text)

#Final option if all else fails
bug_link=driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

#driver.close will close a particular TAB
#driver.quit will close the entire program
# driver.close()
driver.quit()