
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#iframe, frameset, frame
driver.get("https://the-internet.herokuapp.com/iframe")
#frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")

wait = WebDriverWait(driver, 3)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "body[id='tinymce'] p")))
driver.find_element_by_css_selector("body[id='tinymce'] p").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am automating this thing")
driver.switch_to.default_content()

assert "An iFrame containing the TinyMCE WYSIWYG Editor" == driver.find_element_by_tag_name("h3").text

