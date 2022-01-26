from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver.implicitly_wait(10)
# driver.get("https://the-internet.herokuapp.com/dynamic_content")
# driver.find_element_by_link_text("click here").click()
# columns = driver.find_elements_by_css_selector("div[class='large-10 columns']")
# for mama in columns:
#     print(mama.text)


driver.get("https://the-internet.herokuapp.com/dynamic_controls")
check = driver.find_element_by_css_selector("input[type='checkbox']")
check.click()
assert check.is_selected()

presss = driver.find_element_by_css_selector("button[onclick='swapCheckbox()']")
presss.click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//p[@id='message'])[1]")))
message = driver.find_element_by_xpath("(//p[@id='message'])[1]")
assert message.text == "It's gone!"

