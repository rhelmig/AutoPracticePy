from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
url = "http://www.teachmeselenium.com/automation-practice/"


def start_test():
    driver.get(url)
    driver.implicitly_wait(15)
    driver.maximize_window()


# enter user name
def enter_name():
    first_textfield = driver.find_element_by_id('firstname')
    first_textfield.send_keys("Test")
    last_textfield = driver.find_element_by_class_name('lastname')
    last_textfield.send_keys("Test")


# Use the radio button to define gender
def radio_button():
    gender = "//div[@id='content']/article/div/p[7]/input[2]"
    driver.find_element_by_xpath(gender).click()


# check box language
def check_box():
    check = "[name='language_python']"
    driver.find_element_by_css_selector(check).click()


def select_age_list():
    Select(driver.find_element_by_name("age")).select_by_visible_text('Under 20')
    print("Under 20 age was selected.")


# trigger the Submit
def submit():
    driver.find_element_by_id("submit_htmlform").click()


# Get the text of the changing link
def get_text():
    link_text = driver.find_elements_by_partial_link_text("random")
    print(link_text)


# BUG: Alert box is clearing the page data
def get_alert():
    alert_button = driver.find_element_by_link_text("Click Me to get Alert")
    alert_button.click()
    # Switch to the alert box
    alert = driver.switch_to.alert
    # Grab the alert message and print it
    msg = alert.text
    print("Alert shows the following:  " + msg)
    # Accept the alert
    alert.accept()


# Switch to the window 2 and confirm
def switch_window2():
    driver.find_element_by_link_text("Click Me to open New Window").click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    assert '2nd-window' in driver.current_url
    print('Second window was loaded successfully')


# Make drop down selection on second page
def select_list_2():
    Select(driver.find_element_by_id("list-second-window")).select_by_visible_text('Second Window')


# Switch to the window 3 and Confirm
def switch_window3():
    driver.find_element_by_link_text("Click Me To Open Third Window").click()
    window_final = driver.window_handles[2]
    driver.switch_to.window(window_final)
    assert '3rd-window' in driver.current_url
    print('Third window was loaded successfully')


# Make drop down selection for page 3
def select_list_3():
    Select(driver.find_element_by_id("list-third-window")).select_by_visible_text('Third Window')


# End test
def end_test():
    driver.quit()


