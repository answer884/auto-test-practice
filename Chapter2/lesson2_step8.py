from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    input= browser.find_elements(By.CSS_SELECTOR,"[class='form-control']")
    for x in input:
        x.send_keys("TEXT")
    file_button=browser.find_element(By.CSS_SELECTOR,"[id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'example.txt.txt')
    file_button.send_keys(file_path)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR,"[class='btn btn-primary']").click()
finally:
    time.sleep(2)
    browser.quit()
