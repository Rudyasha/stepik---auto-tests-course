import math
from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer").send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
