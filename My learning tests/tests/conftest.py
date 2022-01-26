import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def startingTest(request):
    opt = Options()
    opt.add_argument("--headless")
    global driver
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=opt)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()
