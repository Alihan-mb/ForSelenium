from selenium import webdriver

from pytestsDemo.BaseClass import BaseClass


class TestSomething(BaseClass):
    def test_Canvas(self):
        log = self.getLogger()
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        assert driver.find_element_by_xpath("//p").text == "Congratulations! You must have the proper credentials."

        driver.get("https://the-internet.herokuapp.com/challenging_dom")
        words = driver.find_elements_by_xpath("(//tr)[4]")

        for word in words:
            if word.text == "Definiebas2":
                log.info(word)
                break



