#Js DOM can access any elements on web page like selenium does


from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Hello")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script("return document.getElementsByName('name')[0].value"))

ShopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",ShopButton)
driver.find_element_by_xpath("(//button[@class='btn btn-info'])[1]").click()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")