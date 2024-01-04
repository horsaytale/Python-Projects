from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

GOOGLE_LINK="https://docs.google.com/forms/d/e/1FAIpQLSc2hQCeuqTh3gqcc3Fl8Mdn44TYhT5ZMK_XsGwYTUzBSETMHQ/viewform?usp=sf_link"
CHROME_DRIVER_PATH="C:\Chrome-Driver\chromedriver.exe"
ZILLOW_LINK="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
headers={
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Defined"
}


response=requests.get(ZILLOW_LINK, headers=headers)
zillow_web=response.text

soup=BeautifulSoup(zillow_web,"html.parser")
property_findings=soup.find_all(name="a", class_="list-card-link")
property_values=soup.find_all(name="div", class_="list-card-price")
property_addresses=soup.find_all(name="address",class_="list-card-addr")

property_links=[]
property_prices=[]
property_addr=[]

for finding in property_findings:
    link=finding.get('href')
    if 'https' not in link:
        property_links.append(f"https://www.zillow.com{link}")
    else:
        property_links.append(link)

for value in property_values:
    price=value.text[:-3].replace('+ 1','').replace('+','')
    property_prices.append(price)

for addr in property_addresses:
    property_addr.append(addr.text)

print(property_links)
print(property_prices)
print(property_addr)

driver=webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
driver.get(GOOGLE_LINK)

for i in range(len(property_links)):
    time.sleep(4)
    addr_input=driver.find_elements(By.CLASS_NAME,"quantumWizTextinputPaperinputInput")
    time.sleep(2)
    form_data=[property_addr[i],property_prices[i],property_links[i]]
    for num in range(len(form_data)):
        addr_input[num].send_keys(form_data[num])
        time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
    time.sleep(2)