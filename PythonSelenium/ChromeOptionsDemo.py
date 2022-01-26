from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

box = []
for box in checkboxes:
    if box.get_attribute("value") == "option2":
        box.click()
        assert box.is_selected()

radio = driver.find_elements_by_name("radioButton")
print(len(radio))
radio[2].click()
assert radio[2].is_selected()


assert driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

assert not driver.find_element_by_id("displayed-text").is_displayed()
