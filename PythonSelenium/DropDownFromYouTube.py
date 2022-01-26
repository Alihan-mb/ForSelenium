import time

import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class DemoAutosuggest():
    def demo_autosuggest_dropdown(self, driver):
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        driver.get("https://www.yatra.com/")
        depart_from = driver.find_element_by_id("BE_flight_origin_city")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

dauto = DemoAutosuggest
dauto.demo_autosuggest_dropdown(self.driver)