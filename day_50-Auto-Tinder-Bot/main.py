from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_service=Service("C:\Chrome-Driver\chromedriver.exe")
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://tinder.com/app/recs")

time.sleep(5)
log_in=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

time.sleep(5)
facebook=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()

fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input=driver.find_element(By.NAME,'email')
email_input.send_keys('experi121te89@yahoo.com')

password_input=driver.find_element(By.NAME,'pass')
password_input.send_keys('Lydia@121Maine')

time.sleep(2)
login_button=driver.find_element(By.ID, 'loginbutton')
login_button.click()

time.sleep(3)

driver.switch_to.window(driver.window_handles[0])

time.sleep(5)
allow_location=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_location.click()

time.sleep(2)
allow_notify=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_notify.click()

time.sleep(2)
allow_cookies=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/button')
allow_cookies.click()

time.sleep(2)

for n in range(100):

    time.sleep(4)
    print("called")
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_LEFT)
    actions.perform()

driver.quit()

#to swipe right
# for n in range(100):
#
    # time.sleep(2)
    # print("called")
    # actions = ActionChains(driver)
    # actions.send_keys(Keys.ARROW_RIGHT)
    # actions.perform()
    #
    # time.sleep(2)
    # esc = ActionChains(driver)
    # esc.send_keys(Keys.ESCAPE)
    # esc.perform()