import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
chromedriver_location = "/Users/a913835/Downloads/chromedriver"


driver = webdriver.Chrome(chromedriver_location)
driver.get("https://academymortgage.com/about-us/who-we-are")

test1 = driver.find_element_by_class_name("numbered-cards-section-title")

assert test1.text == "Who We Are", "test1 should be 'Who We Are'"
print("Test 1 passed.")

driver.get("https://academymortgage.com/about-us/what-sets-us-apart")

test2 = driver.find_element_by_id("Main_C002_Col00")

assert test2
print("Test 2 passed.")

driver.get("https://academymortgage.com/about-us/how-we-measure-success")

test3 = driver.find_element_by_id("Main_C002_Col01")

assert test3
print("Test 3 passed.")

driver.get("https://academymortgage.com/about-us/where-we-began")

test4 = driver.find_element_by_class_name("sf-Image-wrapper")

assert test4
print("Test 4 passed.")

driver.get("https://academymortgage.com/about-us/contact-us")

test5 = driver.find_element_by_id("Main_C022_Col00")

assert test5
print("Test 5 passed.")

driver.get("https://academymortgage.com/about-us/apply-now")

name = driver.find_element_by_id("Textbox-1")
email = driver.find_element_by_id("Textbox-2")
phone = driver.find_element_by_id("Textbox-3")
city = driver.find_element_by_id("Textbox-4")
state = Select(driver.find_element_by_id("Dropdown-1"))
zipCode = driver.find_element_by_id("Textbox-5")
loanOfficer = driver.find_element_by_id("Textbox-6")


name.clear()
email.clear()
phone.clear()
city.clear()
zipCode.clear()
loanOfficer.clear()

name.send_keys("jacob")

email.send_keys("jacob.dimick4@gmail.com")

phone.send_keys("7143214655")

city.send_keys("eagle mountain")

state.select_by_visible_text("Utah")
time.sleep(0.8)

zipCode.send_keys("84005")

loanOfficer.send_keys("N/A")