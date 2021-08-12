from selenium import webdriver

chrome_browser = webdriver.Chrome("./chromedriver")

chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
show_msg_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_msg_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_msg = chrome_browser.find_element_by_id('user-message')
chrome_browser.find_element_by_css_selector('#get-input > .btn')
user_msg.clear()
user_msg.send_keys('Sending keys') # mimics typing in that slot.

show_msg_button.click() # simulates clicking that button
output_msg = chrome_browser.find_element_by_id('display')

assert 'Sending keys' in output_msg.text


chrome_browser.close()  # closes current open browser window
chrome_browser.close()  # might have to run twice

chrome_browser.quit()  # closes all tabs(?). might not work depend on versions

# time.wait : makes delays to simulate human activity

