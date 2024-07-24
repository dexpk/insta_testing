import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"\nTest Description: {test.shortDescription()}")
        print("Result: Success\n")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"\nTest Description: {test.shortDescription()}")
        print("Result: Failure")
        print(self.failures[-1][-1])

class TestInstagram(unittest.TestCase):
    
    def setUp(self):
        #Replace Path to your chrome driver
        chrome_driver_path = 'C:/Users/verma/OneDrive/Desktop/Projects/selenium/drivers/chromedriver.exe'
        
        chrome_options = Options()
        chrome_options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        service = Service(chrome_driver_path)
        
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.instagram.com/")
    
    def login(self):
        #Add UserName and Password
        username = "username"
        password = "password"
        
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        WebDriverWait(self.driver, 20).until(EC.url_contains("https://www.instagram.com/accounts/"))
        
        try:
            save_info_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_acan")))
            if save_info_button.is_displayed():
                save_info_button.click()
                
                try:
                    turn_on_notifications_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Turn On']")))
                    if turn_on_notifications_button.is_displayed():
                        turn_on_notifications_button.click()
                except TimeoutException:
                    pass
        
        except TimeoutException:
            pass
    
    def test_like_post(self):
        """
        Test liking a post on Instagram.
        - Navigates to a specific post.
        - Clicks the 'Like' button.
        """
        self.login()
        post_url = "https://www.instagram.com/p/C9mE8nhhubI/"
        self.driver.get(post_url)
        
        # Attempt using class name
        try:
            like_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "x6s0dn4"))
            )
            like_button.click()
            time.sleep(20)
            print("Post liked successfully using class name.")
        except TimeoutException:
            try:
                like_button = self.driver.find_element(By.CLASS_NAME, "x6s0dn4")
                if like_button:
                    print("Like button found but not clickable using class name.")
                else:
                    print("Like button not found using class name.")
            except NoSuchElementException:
                print("Like button not found using class name.")
            self.fail("Like button not found or not clickable using class name.")
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestInstagram('test_like_post'))
    
    runner = unittest.TextTestRunner(resultclass=CustomTestResult)
    runner.run(suite)
