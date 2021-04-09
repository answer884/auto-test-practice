from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link= ("http://suninjuly.github.io/explicit_wait2.html")

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    browser.get(link)
    b= browser.find_element(By.CSS_SELECTOR,"[id='book']")
    button = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), "100")
    )
    b.click()

finally:
    time.sleep(7)
    browser.quit()