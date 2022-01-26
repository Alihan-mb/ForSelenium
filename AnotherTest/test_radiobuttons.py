import time

import pytest
import self
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



@pytest.mark.usefixtures("startingTest")
class Test_this:
    pass

class Test_acctually(Test_this):

    def test_Radion(self):
        log = self.getLogger()
        buttons = self.driver.find_elements_by_name("radioButton")
        log.info("Found the radio button")
        buttons[1].click()
        assert buttons[1].is_selected()
        dropdown = self.driver.find_element_by_id("dropdown-class-example")
        log.info("taken the dropdown")
        dropdownDD = Select(dropdown)
        time.sleep(2)
        listD = dropdownDD.options
        print(len(listD))
        dropdownDD.select_by_visible_text("Option2")
        self.driver.find_element_by_id("autocomplete").send_keys("Ru")
        names = self.driver.find_elements_by_class_name("ui-menu-item")
        print(len(names))
        for name in names:
            print("I found this country", name.text)
            if name.text == "Peru":
                name.click()
                break
        assert self.driver.find_element_by_id("autocomplete").get_attribute('value') == "Peru"