from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector(".nav-link.btn.btn-primary").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()

wait = WebDriverWait(driver, 6)
driver.find_element_by_id("country").send_keys("Russia")
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class='suggestions']")))
driver.find_element_by_css_selector("div[class='suggestions']").click()

checkBox = driver.find_element_by_xpath("//input[@id='checkbox2']")
print(checkBox.is_selected()) # FALSE
assert not checkBox.is_selected()
driver.execute_script("arguments[0].click();",checkBox)
print(checkBox.is_selected()) # True
assert checkBox.is_selected()


Purchase = driver.find_element_by_xpath("//input[@value='Purchase']")
driver.execute_script("arguments[0].click();", Purchase)

textS = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in textS

driver.get_screenshot_as_file("screen.png")