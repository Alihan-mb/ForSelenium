from selenium import webdriver
Spartak = "Option3"
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(Spartak)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
SuperText = alert.text
assert Spartak in SuperText
alert.accept()
print(SuperText)

driver.find_element_by_css_selector("#name").send_keys(Spartak)
driver.find_element_by_id("confirmbtn").click()
mama = alert.text
assert Spartak in mama
alert.dismiss()
print(mama)
