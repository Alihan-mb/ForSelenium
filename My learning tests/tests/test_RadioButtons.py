import time

import pytest
import self
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pytestsDemo.BaseClass import BaseClass

@pytest.mark.usefixtures("startingTest")
class BaseTest:
    pass

class TestPage(BaseTest):

    # @pytest.fixture()
    # def startingTest(self):
    #     opt = Options()
    #     opt.add_argument("--headless")
    #     global driver
    #     driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=opt)
    #     driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    #     driver.implicitly_wait(10)
    #     yield
    #     driver.close()

    def test_Radion(self, startingTest):
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


    def test_windowntabaler(startingTest):
        self.driver.find_element_by_css_selector("button[id*='openwindow']").click()
        secondwindow = self.driver.window_handles[1]
        self.driver.switch_to.window(secondwindow)
        self.driver.find_element_by_xpath("(//ul[@class='nav navbar-nav navbar-right']/li)[2]").click()
        self.driver.find_element(By.XPATH, "(//div[@class='top-right clearfix']/ul/li/a)[1]").click()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        #Тут мы перешли на другую вкладку
        current = self.driver.current_window_handle
        self.driver.find_element_by_id("opentab").click()
        newtab = self.driver.window_handles[1]
        time.sleep(5)
        self.driver.switch_to.window(newtab)
        mama = self.driver.find_element_by_xpath("//h2//span").text
        assert mama == "An Academy to Learn Earn & Shine  in your QA Career", "Test failed because you are an idiot"
        self.driver.close()
        self.driver.switch_to.window(current)
        print("Everything was successful")

        self.driver.find_element_by_name("enter-name").send_keys("Alikhan")
        self.driver.find_element_by_id("alertbtn").click()
        alert = self.driver.switch_to.alert
        texttoverify = alert.text
        assert texttoverify == "Hello Alikhan, share this practice page and share your knowledge", "You've failed again"
        alert.accept()

        self.driver.find_element_by_id("confirmbtn").click()
        anothertext = alert.text
        assert anothertext == "Hello , Are you sure you want to confirm?", "Ha ha, you are a failure"
        alert.dismiss()
        print("You did it you son of a bitch")


    def test_WebScraping(self, startingTest):
        log = self.getLogger()
        names = driver.find_elements_by_xpath("//div[@class='right-align']//div//td[1]")
        amounts = driver.find_elements_by_xpath("//tr/td[4]")
        names_table = []
        amounts_table = []

        for name in names:
            names_table.append(name.text)

        for amount in amounts:
            amounts_table.append(amount.text)

        final = zip(names_table, amounts_table)

        wb = Workbook()
        wb['Sheet'].title="NanNum"
        sh1 = wb.active
        sh1.append(['Names', 'Numbers'])

        for x in list(final):
            sh1.append(x)

        wb.save("WebscrappingExample.xlsx")
        log.info("I've done pasting the info into xlsx file")










