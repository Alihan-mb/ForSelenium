from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/shifting_content/list")

f = driver.find_element_by_xpath("(//div)[7]")
print(f.text)


