import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def selectins_values(options, value):
    if not value[0] == "all":
        for drop in drops:
            for k in range(len(value)):
                if drop.text == value[k]:
                    drop.click()
                    break
    else:
        try:
            for drop in options:
                drop.click()
        except Exception as f:
            print(f)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element_by_id("justAnInputBox").click()
time.sleep(2)

drops = driver.find_elements_by_css_selector("span.comboTreeItemTitle")
#values = ["choice 2", "choice 3", "choice 6"]
values = ["all"]
selectins_values(drops, values)

driver.close()
