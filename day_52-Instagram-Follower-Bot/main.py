from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH="C:\Chrome-Driver\chromedriver.exe"
SIMILAR_ACCOUNTS="chefsteps"
USERNAME="osherji4031"
PASSWORD="0sh8rJ!031"

class InstaFollower:
    def __init__(self,chrome_driver):
        self.driver = webdriver.Chrome(service=Service(chrome_driver))

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        username=self.driver.find_element(By.NAME,"username")
        username.send_keys(USERNAME)

        time.sleep(5)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)

        time.sleep(3)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()

    def find_followers(self):
        time.sleep(5)
        search_input=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search_input.send_keys(SIMILAR_ACCOUNTS)

        time.sleep(10)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()

        time.sleep(5)
        follower_list=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div")
        follower_list.click()
        time.sleep(2)
        #select the pop-up box to scroll down
        modal = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[2]')
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",modal)
            time.sleep(2)

    def followers(self):
        all_buttons=self.driver.find_elements(By.CSS_SELECTOR,".wo9IH button")
        for follower in all_buttons:
            try:
                follower.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot=InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.followers()