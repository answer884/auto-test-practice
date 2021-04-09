from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = ("http://suninjuly.github.io/find_link_text")

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.set_window_size(1920,1080)
    browser.find_element(By.PARTIAL_LINK_TEXT, "592").click()

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='first_name']")
    input1.send_keys('ИВАН')
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='last_name']").send_keys('УРГАНТ')
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys('МОСКВА')
    input4 = browser.find_element(By.CSS_SELECTOR, "[id='country']").send_keys('РОССИЯ')
    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']").click()
finally:
    time.sleep(5)
    browser.quit()