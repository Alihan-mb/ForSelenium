import time

from selenium import webdriver

list = []

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_class_name("search-keyword").send_keys("Ma")
time.sleep(4)
names = driver.find_elements_by_css_selector("h4[class$='product-name']")

for name in names:
    list.append(name.text)

print(list)