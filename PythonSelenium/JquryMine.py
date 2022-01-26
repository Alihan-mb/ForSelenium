import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
# enabled = driver.find_element_by_link_text("Enabled")
# act = ActionChains(driver)
# act.move_to_element(enabled).perform()
# time.sleep(1)
# downloads = driver.find_element_by_link_text("Downloads")
# act.move_to_element(downloads).perform()
# time.sleep(1)
# pdf = driver.find_element_by_link_text("PDF")
# act.move_to_element(pdf).click().perform()

# driver.get("https://the-internet.herokuapp.com/key_presses?")
# target = driver.find_element_by_id("target")
# act = ActionChains(driver)
# act.send_keys(Keys.ENTER).perform()
# time.sleep(1)
# act.send_keys(Keys.UP).perform()
# time.sleep(1)
# act.send_keys(Keys.DOWN).perform()
# time.sleep(1)
# act.send_keys(Keys.BACKSPACE).perform()
# time.sleep(1)
# act.send_keys(Keys.TAB).perform()
# time.sleep(1)
# act.send_keys(Keys.DELETE).perform()
#
# driver.get("https://the-internet.herokuapp.com/large")
# number = driver.find_element_by_xpath("(//*[text() = '42.3'])[1]")
# number1 = driver.find_element_by_xpath("//*[text()='40.9']")
# print(number.text,"And here comes! ", number1.text)


driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(10)
driver.find_element_by_link_text("Click Here").click()
second = driver.window_handles[1]
driver.switch_to.window(second)
time.sleep(1)
message = driver.find_element_by_tag_name("h3")
print(message.text)
first = driver.window_handles[0]
driver.switch_to.window(first)
text = driver.find_element_by_xpath("//h3")
print(text.text)




