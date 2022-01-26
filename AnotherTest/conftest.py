import pytest
from selenium import webdriver

@pytest.fixture()
def init_driver(request):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://the-internet.herokuapp.com/")
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()


@pytest.fixture(scope='class')
def startingTest(request):
    global driver
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()