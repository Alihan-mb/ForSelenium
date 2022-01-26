import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def select_values(options, value):
    if not value[0] == "all":
        for ele in drop:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in options:
                ele.click()
        except Exception as e:
            print(e)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element_by_id("justAnInputBox").click()
time.sleep(2)

drop = driver.find_elements_by_css_selector("span.comboTreeItemTitle")
#value_list = ["choice 2", "choice 3", "choice 6 2 1"]

value_list = ["all"]


select_values(drop, value_list)


# select_values(drop, "choice 3")
# select_values(drop, "choice 6 2 1")







# for ele in drop:
#     print(ele.text)
#     if ele.text == "choice 2":
#         ele.click()
#         break
#

