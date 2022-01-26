from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
driver.find_element_by_id("exampleInputPassword1").send_keys("23FrFFFSDF1412")
driver.find_element_by_name("email").send_keys("Shetty")

mama = Select(driver.find_element_by_id("exampleFormControlSelect1"))
mama.select_by_index(1)

driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type = 'submit']").click()

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message

driver.close()


