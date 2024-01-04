from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_service=Service("C:\Chrome-Driver\chromedriver.exe")

driver=webdriver.Chrome(service=chrome_service)
driver.get("https://www.python.org/")

all_dates=[date.text for date in driver.find_elements(By.CSS_SELECTOR, ".event-widget time")]
print(all_dates)
all_events=[event.text for event in driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')]
print(all_events)

final_dict={i:{"time":all_dates[i],"name":all_events[i]} for i in range(5)}

print(final_dict)

#ANGELA'S SOLUTION
# events={}
# for n in range(len(all_dates)):
#     events[n]={
#         "time":all_dates[n].text,
#         "name":all_events[n].text
#     }
# print(events)

driver.quit()