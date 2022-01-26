from selenium import webdriver

mama = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
mama.get("https://www.youtube.com/")
mama.find_element_by_css_selector("input[name='search_query']").send_keys("Спартак")
mama.find_element_by_id("search-icon-legacy").click()