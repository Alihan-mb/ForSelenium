import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/dynamic_content?with_content=static")
first = driver.find_elements_by_xpath("(//div[@class='large-10 columns'])[1]")
second = driver.find_elements_by_xpath("(//div[@class='large-10 columns'])[2]")
third = driver.find_elements_by_xpath("(//div[@class='large-10 columns'])[3]")

print()