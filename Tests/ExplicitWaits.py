from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# This finds the hidden element, clicks it, then asserts the 'hello world' text is present.
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/dynamic_loading/1")
element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((
    By.XPATH, "//div[@id='start']/button[.='Start']")))
element.click()

assert ("Hello World!", driver.find_element_by_xpath("//div[@id='finish']/h4[.='Hello World!']").text)
