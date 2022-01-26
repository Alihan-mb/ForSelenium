import inspect
import logging

import pytest
from selenium import webdriver


class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    @pytest.fixture()
    def startingTest(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=opt)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.implicitly_wait(10)
        yield
        driver.close()