from selenium.webdriver.support.select import Select
from pytest import mark
# pytest -v --html=report.html


# enter user name
@mark.smoke
def test_enter_name(driver):
    first_textfield = driver.find_element_by_id('firstname')
    first_textfield.send_keys("Test")
    last_textfield = driver.find_element_by_class_name('lastname')
    last_textfield.send_keys("Test")


# Use the radio button to define gender
@mark.smoke
def test_radio_button(driver):
    gender = "//div[@id='content']/article/div/p[7]/input[2]"
    driver.find_element_by_xpath(gender).click()


# check box language
def test_check_box(driver):
    check = "[name='language_python']"
    driver.find_element_by_css_selector(check).click()


def test_select_age_list(driver):
    Select(driver.find_element_by_name("age")).select_by_visible_text('Under 20')
    print("Under 20 age was selected.")


# trigger the Submit
def test_submit(driver):
    driver.find_element_by_id("submit_htmlform").click()


# Get the text of the changing link
def test_get_text(driver):
    link_text = driver.find_elements_by_partial_link_text("random")
    print(link_text)


# BUG: Alert box is clearing the page data
def test_get_alert(driver):
    alert_button = driver.find_element_by_link_text("Click Me to get Alert")
    alert_button.click()
    # Switch to the alert box
    alert = driver.switch_to.alert
    # Grab the alert message and print it
    msg = alert.text
    print("Alert shows the following:  " + msg)
    # Accept the alert
    alert.accept()


# Switch to window 2 and confirm
def test_switch_window2(driver):
    driver.find_element_by_link_text("Click Me to open New Window").click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    assert '2nd-window' in driver.current_url
    print('Second window was loaded successfully')


# Make drop down selection on second page
def test_select_list_2(driver):
    Select(driver.find_element_by_id("list-second-window")).select_by_visible_text('Second Window')


# Switch to window 3 and Confirm
def test_switch_window3(driver):
    driver.find_element_by_link_text("Click Me To Open Third Window").click()
    window_final = driver.window_handles[2]
    driver.switch_to.window(window_final)
    assert '3rd-window' in driver.current_url
    print('Third window was loaded successfully')


# Make drop down selection for page 3
def test_select_list_3(driver):
    Select(driver.find_element_by_id("list-third-window")).select_by_visible_text('Third Window')
