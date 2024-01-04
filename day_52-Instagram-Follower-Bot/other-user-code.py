from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException

chrome_driver_path = "your_chrome_driver_path"
instagram_follow = "instagram_link_to_follow"
my_email = "your_email"
my_password = "your_password"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get(instagram_follow)
        accept_cookies_btn = self.driver.find_element_by_class_name("bIiDR")
        accept_cookies_btn.click()
        time.sleep(2)
        followers_link = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_link.click()
        time.sleep(2)
        email_input = self.driver.find_element_by_css_selector('[name="username"]')
        email_input.send_keys(my_email)
        password_input = self.driver.find_element_by_css_selector('[name="password"]')
        password_input.send_keys(my_password)
        login_btn = self.driver.find_element_by_css_selector('[type="submit"]')
        login_btn.click()
        time.sleep(5)

    def find_followers(self):
        follow_link = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follow_link.click()
        time.sleep(5)

    def follow(self):
        people_to_follow = []
        offset_heigth_all_followers = self.driver.execute_script(
            'return document.querySelector(".isgrP").offsetHeight;')
        total_heigth_all_followers = self.driver.execute_script(
            'return document.querySelector(".isgrP").scrollHeight;')
        new_heigth = offset_heigth_all_followers + 5

        while new_heigth < total_heigth_all_followers:
            follow = self.driver.find_elements_by_css_selector("button.sqdOP")
            people_to_follow.append(follow)

            if total_heigth_all_followers < 1000:  # this number can be changed so it will scroll more and collect more followers
                people_to_follow_extracted = people_to_follow[0]
                time.sleep(2)
                for follower in people_to_follow_extracted:
                    try:
                        time.sleep(2)
                        follower.click()
                        time.sleep(3)
                    except ElementClickInterceptedException:
                        pass
            self.driver.execute_script(f'document.querySelector(".isgrP").scrollTo(0, {new_heigth})')
            new_heigth += 5
            total_heigth_all_followers = self.driver.execute_script(
                'return document.querySelector(".isgrP").scrollHeight;')
            if total_heigth_all_followers > 1000:  # this number can be changed so it will scroll more and collect more followers
                break;
        self.driver.quit()


create_followers = InstaFollower()
create_followers.login()
create_followers.find_followers()
create_followers.follow()