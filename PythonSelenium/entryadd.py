import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

# driver.get("https://the-internet.herokuapp.com/entry_ad")
# time.sleep(2)
# driver.find_element_by_xpath("//div[@class='modal-footer']/p").click()



# driver.get("https://the-internet.herokuapp.com/upload")
# driver.find_element_by_id("file-upload").send_keys("C:/Users/user/Desktop/Waiting.txt")

# driver.get("https://the-internet.herokuapp.com/floating_menu")
# driver.find_element_by_link_text("Elemental Selenium").send_keys(Keys.END)
# time.sleep(2)
# driver.find_element_by_link_text("News").click()


# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element_by_name("username").send_keys("AFFFFFFFFFFFFFFFFF")
# driver.find_element_by_name("password").send_keys("fdsfasdf222")
# time.sleep(2)
# driver.find_element_by_xpath("//button").click()
# time.sleep(2)
# error = driver.find_element_by_css_selector("div[class='flash error']")
# print(error.text)

# driver.get("https://the-internet.herokuapp.com/geolocation")
# driver.find_element_by_css_selector("button[onclick='getLocation()']").click()
# time.sleep(2)
# lat = driver.find_element_by_id("lat-value").text
# long = driver.find_element_by_id("long-value").text
# print(lat)
# assert "46" in str(lat)
# assert "48" in str(long)
# driver.find_element_by_link_text("See it on Google").click()
# print(driver.current_url)

# driver.get("https://the-internet.herokuapp.com/horizontal_slider")
# slider = driver.find_element_by_css_selector("input[type='range']")
# slider.click()
# act = ActionChains(driver)
# time.sleep(2)
# i = 0
# while i < 5:
#     act.send_keys(Keys.ARROW_RIGHT).perform()
#     i = i + 1

# driver.get("https://the-internet.herokuapp.com/hovers")
# pic = driver.find_element_by_xpath("//div[@class='row']//div[2]//img[1]")
# act = ActionChains(driver)
# act.move_to_element(pic).perform()
# time.sleep(2)
# user2 = driver.find_element_by_xpath("//h5[text()='name: user2']").text
# assert "name" in user2
# time.sleep(2)
# link = driver.find_element_by_link_text("View profile")
# act.move_to_element(link).click().perform()
#
# driver.get("https://the-internet.herokuapp.com/infinite_scroll")
# time.sleep(2)
# i = 0
# while i < 1:
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")


# driver.get("https://the-internet.herokuapp.com/inputs")
# n = driver.find_element_by_css_selector("input[type='number']").send_keys("215")
# print(n)
#
# while n < 225:

#
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element_by_css_selector("button[onclick='jsPrompt()']").click()
# alt = driver.switch_to.alert
# alt.send_keys("baba")
# alt.accept()
# result = driver.find_element_by_css_selector("p[id='result']").text
# print(result)
# assert "You entered" in result

driver.get("https://the-internet.herokuapp.com/jqueryui/menu")









