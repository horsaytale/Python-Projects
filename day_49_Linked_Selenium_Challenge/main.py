from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_service=Service("C:\Chrome-Driver\chromedriver.exe")
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

driver.find_element(By.CSS_SELECTOR, ".nav__cta-container .nav__button-secondary").click()

username=driver.find_element(By.ID, "username")
username.send_keys("shie_hui95@hotmail.com")

password=driver.find_element(By.ID, "password")
password.send_keys("L!mSh!eHu!1995")

driver.find_element(By.CSS_SELECTOR, ".login__form_action_container .btn__primary--large").click()

#TO APPLY FOR JOBS
# driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button").click()
# mobile=driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2904064032,43509242,phoneNumber~nationalNumber)"]')
# mobile.send_keys("+60162382895")

#TO SAVE THE JOB
# driver.find_element(By.CLASS_NAME, "jobs-save-button").click()

jobs_list=[job for job in driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")]
print(jobs_list)


for job in jobs_list:
    print("called")
    driver.execute_script("arguments[0].click();",job)
    time.sleep(2)

    try:
        # apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        # apply_button.click()
        # time.sleep(5)
        #
        # # If phone field is empty, then fill your phone number.
        # phone = driver.find_element_by_class_name("fb-single-line-text__input")
        # if phone.text == "":
        #     phone.send_keys("+60162382895")
        #
        # submit_button = driver.find_element_by_css_selector("footer button")
        #
        # # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        # if submit_button.get_attribute("data-control-name") == "continue_unify":
        #     close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        #     close_button.click()
        #     time.sleep(2)
        #     discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
        #     discard_button.click()
        #     print("Complex application, skipped.")
        #     continue
        # else:
        #     submit_button.click()

        # Once application completed, close the pop-up window.
        # time.sleep(2)
        # close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        # close_button.click()
#--------------------------------------------------------------------------------------------
        # apply_button=driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        # driver.execute_script("arguments[0].click();",apply_button)
        # time.sleep(5)
        #
        # phone=driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2904064032,43509242,phoneNumber~nationalNumber)"]')
        # if phone.text=="":
        #     phone.send_keys("+6012382895")
        #
        # cancel_button=driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        # driver.execute_script("arguments[0].click();",cancel_button)
        # discard_button=driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
        # driver.execute_script("arguments[0].click();",discard_button)
#-------------------------------------------------------------------------------------------

        #TO SAVE RATHER THAN APPLY
        save_button=driver.find_element(By.CLASS_NAME, "jobs-save-button")
        driver.execute_script("arguments[0].click();", save_button)

        time.sleep(2)

    except NoSuchElementException:
        print("No application/save button, skipped.")
        continue

time.sleep(5)

driver.quit()