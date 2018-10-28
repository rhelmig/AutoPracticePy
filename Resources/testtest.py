from selenium import webdriver


driver = webdriver.Chrome()
# driver.get("http://www.teachmeselenium.com/automation-practice/")
# driver.implicitly_wait(15)
# driver.maximize_window()
# # enter user name


def enter_name():
    first_textfield = driver.find_element_by_id('firstname')
    first_textfield.send_keys("Test")
    last_textfield = driver.find_element_by_class_name('lastname')
    last_textfield.send_keys("Test")
