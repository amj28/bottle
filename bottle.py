import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def click_play():
    try:
        button_name = 'Welcome-module_button__ZG0Zh'
        button = browser.find_element(By.CLASS_NAME, button_name)
        action = ActionChains(browser)
        action.click(button).perform()

    except:
        print("Play Button not found")

browser = webdriver.Firefox()
browser.get('https://www.nytimes.com/games/wordle/index.html')

time.sleep(2) # wait for 3 seconds

try:    
    button_name = 'purr-blocker-card__button'
    button = browser.find_element(By.CLASS_NAME, button_name)
    action = ActionChains(browser)
    action.click(button).perform()

except:
    print("Purr Button not found")

time.sleep(2)

click_play()

time.sleep(1)

browser.execute_script('window.history.back()')
time.sleep(1)
click_play()

