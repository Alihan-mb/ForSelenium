from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_avito():
    def test_Avito(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.avito.ru/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//div[@data-id='83']").click()
        self.driver.find_element(By.LINK_TEXT, "Посмотреть").click()

        parent = self.driver.window_handles[0]
        second = self.driver.window_handles[1]

        self.driver.switch_to.window(second)

        self.driver.find_element(By.NAME, "locationOfCompletion").send_keys("Астрахань")
        self.driver.find_element(By.NAME, "dateOfCompletion").send_keys("14022022")

        percentage = self.driver.find_element(By.XPATH, "//span[@class='desktop-1efus0k']")

        assert percentage.text == "4%"
        self.driver.close()
        self.driver.switch_to.window(parent)
        self.driver.quit()

    def test_AvitoIteration(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.avito.ru/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        print(self.driver.execute_script("return navigator.userAgent;"))
        self.driver.find_element(By.LINK_TEXT, "Транспорт").click()
        self.driver.find_element(By.LINK_TEXT, "Автомобили").click()
        point_to_scroll = self.driver.find_element(By.XPATH, "//li[@class='multi-select-car-body-item-mfAp8']")
        self.driver.execute_script("arguments[0].scrollIntoView()", point_to_scroll)

        names = self.driver.find_elements(By.XPATH, "//h3[@itemprop='name']")

        for name in names:
            print("Here is an option", name.text)
            if name.text == "Toyota Camry, 2018":
                name.click()
                break

        item_name = self.driver.find_element(By.XPATH, "//h1")

        assert item_name.text == "Toyota Camry, 2018"


















