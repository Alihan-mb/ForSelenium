import time
from logging import getLogger

import pytest
from _pytest.fixtures import fixture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pytestsDemo.BaseClass import BaseClass



class TestAuth(BaseClass):
    @pytest.fixture()
    def basics_fortest(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        driver.implicitly_wait(10)

    # def test_Auth(self, basics_fortest):
    #     driver.get("https://www.facebook.com/")
    #     driver.implicitly_wait(10)
    #     driver.find_element_by_xpath("//*[text()='Создать новый аккаунт']").click()
    #     driver.find_element_by_name("firstname").send_keys("Mmama")
    #     driver.find_element_by_name("lastname").send_keys("Mububu")
    #     driver.find_element_by_name("reg_email__").send_keys("hvh-mb@gmail.ru")
    #     driver.find_element_by_name("reg_email_confirmation__").send_keys("hvh-mb@gmail.ru")
    #     driver.find_element_by_id("password_step_input").send_keys("Mambersdf")
    #
    #     day=Select(driver.find_element_by_xpath("//select[@title='День']"))
    #     day.select_by_visible_text("10")
    #     month=Select(driver.find_element_by_name("birthday_month"))
    #     month.select_by_visible_text("июл")
    #     year=Select(driver.find_element_by_name("birthday_year"))
    #     year.select_by_visible_text("2000")
    #     driver.find_element_by_xpath("//label[text()='Мужчина']").click()
    #     driver.find_element_by_xpath("//button[@name='websubmit']").click()


    def test_frame(self, basics_fortest):
        log = getLogger()
        driver.get("https://www.redbus.in/")
        driver.maximize_window()
        driver.find_element_by_class_name("icon-profile-new-unsigned ").click()
        driver.find_element_by_id("signInLink").click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='modalIframe']"))
        driver.switch_to.parent_frame()
        driver.find_element_by_css_selector("i[class='icon-close']").click()


        # mainW = driver.window_handles[0]
        # secondW = driver.window_handles[1]
        # driver.switch_to.window(secondW)
        # driver.find_element_by_xpath("//div[@role='listbox']").click()
        # driver.find_element_by_xpath("(//div[@data-value='de'])[2]").click()
        # driver.close()
        # driver.switch_to.window(mainW)
        # driver.find_element_by_class_name("icon-close").click()

        driver.find_element_by_css_selector("input[type='text']").send_keys("Ma")

        names = driver.find_elements_by_xpath("//ul[@class='autoFill homeSearch']/child::li")
        print(len(names))

        for name in names:
            if "Madurai" == name.text:
                name.click()
                break













