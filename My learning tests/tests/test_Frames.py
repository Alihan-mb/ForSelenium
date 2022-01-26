import time

import action
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from pytestsDemo.BaseClass import BaseClass


class TestFrames(BaseClass):
    @pytest.fixture()
    def startingTest(self):
        global driver
        opt = Options()
        opt.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=opt)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.implicitly_wait(10)
        yield
        driver.close()

    def test_displayed(self, startingTest):
        log = self.getLogger()
        element = driver.find_element_by_id("displayed-text")
        assert element.is_displayed()
    def test_frames(self, startingTest):
        log = self.getLogger()
        driver.execute_script("window.scrollTo(0,1400);")
        driver.switch_to.frame(driver.find_element_by_id("courses-iframe"))
        over = driver.find_element_by_xpath("(//a[@data-toggle='dropdown'])[1]")
        act = ActionChains(driver)
        act.move_to_element(over).perform()
        time.sleep(2)
        driver.find_element_by_xpath("(//a[text()='About us'])[1]").click()

        driver.switch_to.parent_frame()
        time.sleep(2)
        driver.execute_script("window.scroll(0,0)")
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='Home']").click()




