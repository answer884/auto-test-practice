from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link=('http://suninjuly.github.io/selects1.html')

try:
    browser= webdriver.Chrome()
    browser.get(link)
    x= int(browser.find_element(By.CSS_SELECTOR,"[id='num1']").text) + int(browser.find_element(By.CSS_SELECTOR,"[id='num2']").text)
    select1= Select(browser.find_element(By.CSS_SELECTOR,"[id='dropdown']"))

    select1.select_by_visible_text(str(x))
    time.sleep(1)
    browser.find_element(By.CLASS_NAME,'btn.btn-default').click()
finally:
    time.sleep(2)
    browser.quit()