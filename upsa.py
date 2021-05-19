from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()
    browser.find_element_by_id("button")
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    number = browser.find_element_by_id("input_value").text
    result = calc(int(number))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    btn = browser.find_element_by_tag_name("button")
    btn.click()

finally:

    time.sleep(10)
    browser.quit()