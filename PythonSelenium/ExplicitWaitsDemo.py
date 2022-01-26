# implicit wait
# Explicit wait
# pause the test for few second using time class
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

list = []
list2 = []

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/ div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    #print(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

for names in buttons:
    list.append(names.find_element_by_xpath("parent::div/parent::div/h4").text)

print(list)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[class='promoCode']")))
products = driver.find_elements_by_css_selector("p[class='product-name']")

for veg in products:
    list2.append(veg.text)

print(list2)
assert list == list2

price = driver.find_element_by_css_selector("span.discountAmt").text
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)
price2 = driver.find_element_by_xpath("//span[contains(@class,'discountAmt')]").text
assert int(price) > float(price2)

values = driver.find_elements_by_xpath("//tr/td[5]/p")
summ = 0
for value in values:
    summ = summ + int(value.text)

print(summ)

TotAMT = driver.find_element_by_css_selector("span.totAmt").text

assert summ == int(TotAMT)












