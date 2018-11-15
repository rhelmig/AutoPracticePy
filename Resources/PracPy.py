from selenium import webdriver
from selenium.webdriver.support.select import Select

'''
Strictly Python run through of AUT.
'''

# setup
driver = webdriver.Chrome()
driver.get("http://www.teachmeselenium.com/automation-practice/")
driver.implicitly_wait(5)
driver.maximize_window()


# enter user name
first_textfield = driver.find_element_by_id('firstname')
first_textfield.send_keys("Test")
last_textfield = driver.find_element_by_class_name('lastname')
last_textfield.send_keys("Test")

# Use the radio button to define gender
gender = "//div[@id='content']/article/div/p[7]/input[2]"
gender_select = driver.find_element_by_xpath(gender).click()

# check box language
check = "[name='language_python']"
py_check = driver.find_element_by_css_selector(check).click()


# select drop down option for age range.  Added class and function for no specific reason.
Select(driver.find_element_by_name("age")).select_by_visible_text('Under 20')
print("Under 20 age was selected.")

# trigger the Submit
driver.find_element_by_id("submit_htmlform").click()

# Get the text of the changing link
link_text = driver.find_elements_by_partial_link_text("random")
print(link_text)

'''
Trigger an alert, confirm text, dismiss
BUG: Alert box is clearing the page data
'''
alert_button = driver.find_element_by_link_text("Click Me to get Alert")
alert_button.click()
# Switch to the alert box
alert = driver.switch_to.alert
# Grab the alert message and print it
msg = alert.text
print("Alert shows the following:  " + msg)
# Accept the alert
alert.accept()

# Switch to the window 2
window_before = driver.window_handles[0]
driver.find_element_by_link_text("Click Me to open New Window").click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

# Confirm Second Window loaded
assert '2nd-window' in driver.current_url
print('Second window was loaded successfully')

# Make drop down selection on second page
Select(driver.find_element_by_id("list-second-window")).select_by_visible_text('Second Window')

# Switch to the window
window_next = driver.window_handles[1]
driver.find_element_by_link_text("Click Me To Open Third Window").click()
window_final = driver.window_handles[2]
driver.switch_to.window(window_final)

# Make drop down selection for page 3
Select(driver.find_element_by_id("list-third-window")).select_by_visible_text('Third Window')

# Confirm Second Window loaded
assert '3rd-window' in driver.current_url
print('Third window was loaded successfully')
