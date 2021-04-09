from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link=('http://suninjuly.github.io/get_attribute.html')

try:
    browser= webdriver.Chrome()
    browser.get(link)
    browser.set_window_size(1920,1080)

    val=browser.find_element(By.ID,"treasure")
    y= val.get_attribute('valuex')
    x=calc(y)
    browser.find_element(By.CSS_SELECTOR,"[id='answer']").send_keys(x)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    time.sleep(3)
    browser.find_element_by_class_name("btn.btn-default").click()
finally:
    time.sleep(5)
    browser.quit()