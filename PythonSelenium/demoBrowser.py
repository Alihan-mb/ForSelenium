from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we need to invoke the \
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
fire_options = webdriver.FirefoxOptions()
fire_options.add_argument("headless")
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=fire_options)

#driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/") #get

print(driver.title)
print(driver.current_url)
driver.get("https://courses.rahulshettyacademy.com/courses")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close() #closes only the current window






