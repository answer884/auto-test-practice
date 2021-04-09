from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link= ("http://suninjuly.github.io/registration1.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.set_window_size(1980,1920)
    browser.find_element(By.CSS_SELECTOR,"[placeholder='Input your first name']").send_keys('ROMAN')
    browser.find_element(By.CSS_SELECTOR,"[placeholder='Input your last name']").send_keys('BELUGA')
    browser.find_element(By.CSS_SELECTOR,"[placeholder='Input your email']").send_keys('belugalyga@beluga.com')
    browser.find_element_by_class_name("btn.btn-default").click()
    time.sleep(2)
    welcome_text=browser.find_element(By.CSS_SELECTOR,"[class='container'] > h1")
    text1= welcome_text.text

    assert "Congratulations! You have successfully registered!" == text1

finally:
    time.sleep(2)
    browser.quit()