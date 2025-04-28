from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time


class TestLogin:

    def setup_class(self):
       global driver
       chrome_options = Options()
       chrome_options.add_argument("--incognito")
       driver = webdriver.Chrome(options=chrome_options)
       driver.maximize_window()
       
    
    def test_login(self):
       driver.get('https://github.com')
    
       btn_signin = driver.find_element(By.CLASS_NAME,'HeaderMenu-link--sign-in')
       btn_signin.click()

       time.sleep(2)

       field_login = driver.find_element(By.ID,'login_field')
       field_login.send_keys('test.script4iz@gmail.com')

       field_password = driver.find_element(By.ID,'password')
       field_password.send_keys('Test9090')

       field_password.send_keys(Keys.RETURN)

       time.sleep(2)

       driver.save_screenshot('FinalShot.png')

    
       label_result = driver.find_element(By.CLASS_NAME, 'js-flash-alert')
       print(label_result.text)
       # Passed
       #assert 'Incorrect username or password.' in label_result.text
       # Failed
       assert 'Incorrrect usernamepassword' in label_result.text



    def teardown_class(self):
        driver.close()