#!/usr/bin/env python3

from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
import openpyxl
from selenium.common.exceptions import NoSuchElementException


def write_links_excel(linkinfo):
    wb = openpyxl.Workbook()
    sheet = wb.active
    c1 = sheet.cell(row=1, column=1)
    c1.value = linkinfo
    wb.save(r'C:\Users\Nihaan\Desktop\brokenlinks.xlsx')


op = webdriver.ChromeOptions()
op.headless = True
driver = webdriver.Chrome(chrome_options=op)

url = "https://www.google.com/"
driver.get(url)
try:
    links = driver.find_elements(By.TAG_NAME, "a")
except NoSuchElementException:
    print(" no element")
for link in links:
    href = link.get_attribute('href')
    status_code = requests.head(href).status_code
    if status_code == 200:
        print(f"valid link:{href}")
    elif status_code in (301, 302):
        print(f"redirected: {href}")
    else:
        print(f"not valid link: status_code is {status_code} : {href}")
        broken_links = href
        write_links_excel(href)
