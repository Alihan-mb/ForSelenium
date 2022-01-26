import action as action
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
mouserhover = driver.find_element_by_id("mousehover")
action.move_to_element(mouserhover).perform()
Top = driver.find_element_by_link_text("Top")
Reload = driver.find_element_by_link_text("Reload")
action.move_to_element(Top).click().perform()

action = ActionChains(driver)
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
action.context_click(driver.find_element_by_css_selector("button[ondblclick='myFunction()']")).perform()
action.double_click(driver.find_element_by_css_selector("button[ondblclick='myFunction()']")).perform()

alert = driver.switch_to.alert
assert "You double clicked me.. Thank You.." == alert.text
alert.accept()