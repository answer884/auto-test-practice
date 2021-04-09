from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(y):
    return str(math.log(abs(12 * math.sin(int(x)))))

link= ("http://suninjuly.github.io/execute_script.html")

try:
    browser= webdriver.Chrome()
    browser.get(link)
    browser.set_window_size(1920,1080)
    x=browser.find_element(By.ID,"input_value").text
    field= browser.find_element(By.CSS_SELECTOR,"[id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(calc(int(x)))
    browser.execute_script("window.scrollBy(0, 50);")
    browser.find_element(By.CSS_SELECTOR,"[id='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR,"[id='robotsRule']").click()
    browser.find_element(By.CSS_SELECTOR,"[class='btn btn-primary']").click()
finally:
    time.sleep(5)
    browser.quit()

