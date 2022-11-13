from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()
    #1. go to google.com
    driver.get("http://www.google.com")
    #1.1 click the reject all button in the cookie cosent form
    driver.find_element(By.ID,'W0wltc').click()
    #2. type in a search ' puppies'
    driver.find_element(By.NAME,"q").send_keys('puppies' + Keys.RETURN)

    #4. assert we landed on a search page for puppies
    assert 'puppies' in driver.title