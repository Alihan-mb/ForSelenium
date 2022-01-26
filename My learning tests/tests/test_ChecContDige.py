from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.get("https://the-internet.herokuapp.com/context_menu")
# action = ActionChains(driver)
# action.context_click(driver.find_element_by_css_selector("div[id='hot-spot']")).perform()
# alert = driver.switch_to.alert
# mama = alert.text
# assert mama == "You selected a context menu"
# alert.accept()

# driver.get("https://the-internet.herokuapp.com/disappearing_elements")
# driver.find_element_by_link_text("Home").click()
# driver.back()
# driver.find_element_by_link_text("About").click()
# driver.back()
# driver.find_element_by_link_text("Contact Us").click()
# driver.back()
#
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# b = driver.find_element_by_xpath("//input[2]")
# assert b.is_selected()
# n = driver.find_element_by_xpath("//input[1]")
# n.click()
# assert n.is_selected()


# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
#
# A = driver.find_element_by_css_selector("div[id='column-b']")
# B = driver.find_element_by_css_selector("div[id='column-a']")
#
# drag = ActionChains(driver)
# drag.drag_and_drop(B, A).perform()
















