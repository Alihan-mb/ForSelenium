from selenium import webdriver

def test_sca():
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://the-internet.herokuapp.com/dynamic_content")
    columns = driver.find_elements_by_class_name("large-10 columns")
    for column in columns:
        print(column.text)