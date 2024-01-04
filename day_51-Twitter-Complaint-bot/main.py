from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN= 100
PROMISED_UP= 30
CHROME_DRIVER_PATH="C:\Chrome-Driver\chromedriver.exe"
TWITTER_EMAIL="experi121te89@yahoo.com"
TWITTER_PASSWORD="20SH8rJ!031"

class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver):
        self.driver = webdriver.Chrome(service=Service(chrome_driver))
        self.down=0
        self.up=0

    def get_internet_speed(self):
        bot.driver.get("https://www.speedtest.net/")

        go_button = bot.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()

        time.sleep(60)
        self.down = float(bot.driver.find_element(By.CLASS_NAME, "download-speed").text)

        self.up = float(bot.driver.find_element(By.CLASS_NAME, "upload-speed").text)

        #Another Method which is more convenient for users - awaits for load to be done before excuted
        #next code

        # loading = True
        # while loading:
        #
        #     upload1 = bot.driver.find_element(By.CLASS_NAME, "upload-speed").text
        #     download1 = bot.driver.find_element(By.CLASS_NAME, "download-speed").text
        #     time.sleep(3)
        #
        #     if upload1 != " " and download1 != " ":
        #         self.up = float(upload1)
        #         self.down = float(download1)
        #
        #         loading = False

    def tweet_at_provider(self):
        time.sleep(4)
        bot.driver.get("https://twitter.com/i/flow/login")

        time.sleep(4)
        username = bot.driver.find_element(By.TAG_NAME, value='input')
        username.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        username.send_keys(Keys.ENTER)

        time.sleep(4)
        verify=bot.driver.find_element(By.TAG_NAME, value='input')
        verify.send_keys("HuOsher")
        time.sleep(2)
        verify.send_keys(Keys.ENTER)

        time.sleep(4)
        password_input = bot.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)

        time.sleep(4)
        tweet_input = bot.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")

        if self.down < PROMISED_DOWN and self.up < PROMISED_UP:
            tweet_input.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

            time.sleep(2)
            bot.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]").click()
        else:
            tweet_input.send_keys(f"Hello Internet Provider, some pretty decent speeds today {self.down} download/ {self.up} upload, keep it up!")
            time.sleep(2)
            bot.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]").click()

        time.sleep(3)
        self.driver.quit()

bot=InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# bot.get_internet_speed()
bot.tweet_at_provider()



