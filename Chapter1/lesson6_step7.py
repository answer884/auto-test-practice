from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = ("http://suninjuly.github.io/huge_form.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input= browser.find_elements(By.CSS_SELECTOR,"[required]")

    for element in input:
        element.send_keys('Мой ответ')
    button = browser.find_element(By.CSS_SELECTOR,"[class='btn btn-default']").click()
finally:
    time.sleep(10)
    browser.quit()
    driver.clouse()