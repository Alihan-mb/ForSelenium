import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.yatra.com/")
driver.implicitly_wait(5)
depart_from = driver.find_element_by_id("BE_flight_origin_city")
depart_from.click()
depart_from.send_keys("New Delhi")
depart_from.send_keys(Keys.ENTER)
going_to = driver.find_element_by_id("BE_flight_arrival_city")
going_to.send_keys("New")
search_results = driver.find_elements_by_xpath("//div[@class='viewport']//div[1]/li")
print(len(search_results))

for results in search_results:
    if "New York (JFK)" in results.text:
        results.click()
        time.sleep(4)
        break