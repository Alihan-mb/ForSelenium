from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/si/Downloads/chromedriver')
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_class_name("search-keyword").send_keys("ber")
list = []

# driver.find_element_by_css_selector("//div[@class='product']")
hey = driver.find_elements_by_xpath("//div[@class='product']/div/parent::div/h4")
for p in hey:
    list.append(p.text)
print(list)
