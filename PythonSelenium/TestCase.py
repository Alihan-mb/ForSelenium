from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
name = driver.find_element_by_xpath("(//h4[@class='card-title']/a)[4]").text

driver.find_element_by_xpath("(//button[@class='btn btn-info']) [4]").click()
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".nav-link.btn.btn-primary")))
driver.find_element_by_css_selector(".nav-link.btn.btn-primary").click()

aname = driver.find_element_by_xpath("(//a[@href='#']) [4]").text

assert name == aname

driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Russia")
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class='suggestions']")))
driver.find_element_by_css_selector("div[class='suggestions']").click()

driver.find_element_by_xpath("//label[@for='checkbox2']").click()
driver.find_element_by_xpath("//input[@value='Purchase']").click()
sactual = driver.find_element_by_class_name("alert alert-success alert-dismissible").text

alert = driver.switch_to.alert
actual = alert.text

assert actual == sactual

alert.dismiss()

#div[class='checkbox checkbox-primary']