from openpyxl import Workbook
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/redirector")
driver.find_element_by_link_text("here").click()
driver.find_element_by_link_text("here").click()

codes = driver.find_elements_by_xpath("//td[@align='center']")
desc = driver.find_elements_by_xpath("//tr//td[2]")
links = driver.find_elements_by_xpath("//tr//td//a")

codes_table = []
desc_table = []
links_table = []

for code in codes:
    codes_table.append(code.text)

for d in desc:
    desc_table.append(d.text)

for link in links:
    links_table.append(link.text)


result = zip(codes_table, desc_table, links_table)

excel = Workbook()
excel['Sheet'].title = "Here"
sh1 = excel.active
sh1.append(['Names', 'Numbers', 'Links'])

for x in list(result):
    sh1.append(x)

excel.save("HerokacExample.xlsx")

driver.close()