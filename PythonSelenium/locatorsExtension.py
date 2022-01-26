from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("input#username").send_keys("Alihan")
driver.find_element_by_css_selector("input.password").send_keys("1232234")
driver.find_element_by_css_selector("input.password").clear()
driver.find_element_by_css_selector("a[id='forgot_password_link']").click()
driver.find_element_by_name("cancel").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
driver.close()