from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(y):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = ('http://suninjuly.github.io/alert_accept.html')

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR,"[class='btn btn-primary']").click()
    alle= browser.switch_to.alert
    alle.accept()
    time.sleep(1)
    x=browser.find_element(By.CSS_SELECTOR,"[id='input_value']").text
    browser.find_element(By.CSS_SELECTOR,"[id='answer']").send_keys(calc(int(x)))
    browser.find_element(By.CSS_SELECTOR,"[class='btn btn-primary']").click()
finally:
    time.sleep(2)
    browser.quit()


