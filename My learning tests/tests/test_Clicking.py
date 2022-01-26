import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text("Add/Remove Elements").click()
mama = driver.find_elements_by_css_selector("button[onclick='addElement()']")

number = 1
while number < 6:
    for mam in mama:
        mam.click()

    number = number+1

papa = driver.find_elements_by_css_selector("button[class='added-manually']")

i = 1

while i < 5:
    for pap in papa:
        if pap.is_displayed():
            pap.click()
    break

