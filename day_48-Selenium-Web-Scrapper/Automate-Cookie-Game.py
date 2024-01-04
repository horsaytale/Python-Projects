from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_service=Service("C:\Chrome-Driver\chromedriver.exe")
driver=webdriver.Chrome(service=chrome_service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID,"cookie")
# addons=[addon.text for addon in driver.find_elements(By.CSS_SELECTOR,"#store div")]
items=driver.find_elements(By.CSS_SELECTOR,"#store div")
item_ids=[item.get_attribute("id") for item in items]
print(item_ids)

five_minute=time.time()+60*5
timeout=time.time()+5

while True:
    cookie.click()
    #Every 5 seconds
    if time.time()>timeout:

        all_prices=driver.find_elements(By.CSS_SELECTOR,"#store div b")
        item_prices=[]

        for price in all_prices:
            element_text=price.text
            if element_text!="":
                cost=int(price.text.split()[-1].replace(',',''))
                item_prices.append(cost)

        #Create a dictionary of store items and prices
        cookie_upgrades={}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]]=item_ids[n]

        #Get current cookie amount
        cookie_count=int(driver.find_element(By.ID, "money").text.replace(",",''))

        #Find affordable upgrades
        affordable_upgrades={}
        for cost,id in cookie_upgrades.items():
            if cookie_count>cost:
                affordable_upgrades[cost]=id

        #Purchase the most expensive affordable upgrade
        highest_price=max(affordable_upgrades)
        print(highest_price)
        to_purchase_id=affordable_upgrades[highest_price]

        driver.find_element(By.ID,to_purchase_id).click()

        #Add another 5 seconds until next check
        #I assume once the 5 secs done, timeout=0, no reason to continue, therefore, add more 5secs
        timeout=time.time()+5

    if time.time()>five_minute:
        cookie_per_s=driver.find_element(By.ID,"cps").text
        print(cookie_per_s)
        break



