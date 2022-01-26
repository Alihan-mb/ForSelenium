import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.tutu.ru/")
driver.find_element_by_xpath("//div[@class='b-counter__places__standart _little j-passenger_full s-min']/div[@class='increase']").click()





