import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
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

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        #Add Path to your chrome drive
        chrome_driver_path = 'C:/Users/verma/OneDrive/Desktop/Projects/selenium/drivers/chromedriver.exe'
        
        chrome_options = Options()
        chrome_options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        service = Service(chrome_driver_path)
        
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.instagram.com/")
    
    def login(self):
        #Add username and password
        username = "username"
        password = "password"
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        WebDriverWait(self.driver, 10).until(EC.url_contains("https://www.instagram.com/accounts/"))
        
        try:
            save_info_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "_acan")))
            if save_info_button.is_displayed():
                save_info_button.click()
                
                try:
                    turn_on_notifications_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Turn On']")))
                    if turn_on_notifications_button.is_displayed():
                        turn_on_notifications_button.click()
                except TimeoutException:
                    pass
        
        except TimeoutException:
            pass

    # def test_login_valid_credentials(self):
    #     """
    #     Test Instagram login with valid credentials.
    #     - Enters valid username and password.
    #     - Clicks login button.
    #     - Handles optional 'Save Info' and 'Turn On Notifications' pop-ups if they appear.
    #     """
    #     self.login()

    # def test_login_invalid_credentials(self):
    #     """
    #     Test Instagram login with invalid credentials.
    #     - Enters invalid username and password.
    #     - Clicks login button.
    #     - Verifies error message for incorrect password.
    #     """
    #     username = "invalid_username"
    #     password = "invalid_password"
        
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
    #     username_field = self.driver.find_element(By.NAME, "username")
    #     password_field = self.driver.find_element(By.NAME, "password")
    #     login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        
    #     username_field.send_keys(username)
    #     password_field.send_keys(password)
    #     login_button.click()
        
    #     try:
    #         error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@id='slfErrorAlert']")))
    #         error_text = error_message.text
    #         self.assertIn("Sorry, your password was incorrect.", error_text)
    #     except TimeoutException:
    #         pass
    
    # def test_login_empty_username(self):
    #     """
    #     Test Instagram login with empty username field.
    #     - Leaves username field empty.
    #     - Enters valid password.
    #     - Attempts login and verifies error message for empty username field.
    #     """
    #     password = "password"
        
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
    #     password_field = self.driver.find_element(By.NAME, "password")
    #     login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        
    #     password_field.send_keys(password)
    #     login_button.click()
        
    #     try:
    #         error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@id='slfErrorAlert']")))
    #         error_text = error_message.text
    #         self.assertIn("The username field is required.", error_text)
    #     except TimeoutException:
    #         pass
    
    # def test_decline_notifications(self):
    #     """
    #     Test declining notifications during Instagram login.
    #     - Logs in with valid credentials.
    #     - Handles optional 'Save Info' and 'Turn On Notifications' pop-ups.
    #     - Declines 'Turn On Notifications' if presented.
    #     """
    #     self.login()
        
    #     try:
    #         save_info_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "_acan")))
    #         if save_info_button.is_displayed():
    #             save_info_button.click()
                
    #             try:
    #                 turn_on_notifications_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Turn On']")))
    #                 if turn_on_notifications_button.is_displayed():
    #                     turn_on_notifications_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
    #                     turn_on_notifications_button.click()
    #             except TimeoutException:
    #                 pass
        
    #     except TimeoutException:
    #         pass
    
    # def test_follow_user(self):
    #     """
    #     Test following a user on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to a user's profile.
    #     - Clicks follow button.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/piyushp_k_y/")
        
    #     follow_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Follow']")))
    #     follow_button.click()
    #     time.sleep(200)
    
    # def test_unfollow_user(self):
    #     """
    #     Test unfollowing a user on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to a user's profile.
    #     - Clicks unfollow button.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/piyushp_k_y/")
        
    #     unfollow_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Following']")))
    #     unfollow_button.click()
        
    #     confirm_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Unfollow']")))
    #     confirm_button.click()
    
    # def test_post_comment(self):
    #     """
    #     Test posting a comment on a post.
    #     - Logs in with valid credentials.
    #     - Navigates to a post.
    #     - Enters and posts a comment.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/p/C9mE8nhhubI/")
        
    #     comment_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[aria-label='Add a comment…']")))
    #     comment_field.click()
    #     comment_field.send_keys("Nice post!")
        
    #     post_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Post']")))
    #     post_button.click()
    
    # def test_like_post(self):
    #     """
    #     Test liking a post on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to a post.
    #     - Clicks like button.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/p/C9mE8nhhubI/")
        
    #     like_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Like']")))
    #     like_button.click()
    
    # def test_unlike_post(self):
    #     """
    #     Test unliking a post on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to a post.
    #     - Clicks unlike button.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/p/C9mE8nhhubI/")
        
    #     unlike_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Unlike']")))
    #     unlike_button.click()
    
    # def test_update_profile_picture(self):
    #     """
    #     Test updating profile picture on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to profile page.
    #     - Uploads a new profile picture.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/accounts/edit/")
        
    #     change_profile_pic_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Change Profile Photo']")))
    #     change_profile_pic_button.click()
        
    #     upload_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='file']")))
    #     upload_button.send_keys("/home/dexy/instagram_automation/image/post.png")
    
    # def test_update_bio(self):
    #     """
    #     Test updating bio on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to profile page.
    #     - Updates bio text.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/accounts/edit/")
    #     time.sleep(200)
        
    #     bio_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "biography")))
    #     bio_field.clear()
    #     bio_field.send_keys("This is my new bio!")
        
    #     submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
    #     submit_button.click()
    
    # def test_update_website(self):
    #     """
    #     Test updating website link on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to profile page.
    #     - Updates website link.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/accounts/edit/")
        
    #     website_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "external_url")))
    #     website_field.clear()
    #     website_field.send_keys("https://www.example.com")
        
    #     submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
    #     submit_button.click()
    
    # def test_view_story(self):
    #     """
    #     Test viewing a story on Instagram.
    #     - Logs in with valid credentials.
    #     - Clicks on the first story on the home page.
    #     """
    #     self.login()
        
    #     first_story = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@aria-label, 'Your Story')]")))
    #     first_story.click()
    
    # def test_send_message(self):
    #     """
    #     Test sending a direct message on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to direct messages.
    #     - Sends a message to a user.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/direct/inbox/")
        
    #     new_message_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='New Message']")))
    #     new_message_button.click()
        
    #     search_user_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "queryBox")))
    #     search_user_field.send_keys("cristiano")
        
    #     user_result = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='cristiano']")))
    #     user_result.click()
        
    #     next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
    #     next_button.click()
        
    #     message_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Message...']")))
    #     message_field.send_keys("Hello, Cristiano!")
        
    #     send_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Send']")))
    #     send_button.click()
    
    # def test_view_followers(self):
    #     """
    #     Test viewing followers on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to profile page.
    #     - Clicks on followers to view the list.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/automationinsta1/")
        
    #     followers_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]")))
    #     followers_button.click()
    
    # def test_view_following(self):
    #     """
    #     Test viewing following list on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to profile page.
    #     - Clicks on following to view the list.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/automationinsta1/")
        
    #     following_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/following/')]")))
    #     following_button.click()
    
    def test_search_user(self):
        """
        Test searching for a user on Instagram.
        - Logs in with valid credentials.
        - Uses the search bar to search for a user.
        """
        self.login()
        
        search_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
        search_field.send_keys("cristiano")
        
        search_result = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/cristiano/']")))
        search_result.click()
        time.sleep(200)
    
    # def test_block_user(self):
    #     """
    #     Test blocking a user on Instagram.
    #     - Logs in with valid credentials.
    #     - Navigates to a user's profile.
    #     - Blocks the user.
    #     """
    #     self.login()
        
    #     self.driver.get("https://www.instagram.com/cristiano/")
        
    #     options_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Options']")))
    #     options_button.click()
        
    #     block_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Block']")))
    #     block_button.click()
        
    #     confirm_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Block']")))
    #     confirm_button.click()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(TestLogin('test_login_valid_credentials'))
    # suite.addTest(TestLogin('test_login_invalid_credentials'))
    # suite.addTest(TestLogin('test_login_empty_username'))
    # suite.addTest(TestLogin('test_decline_notifications'))
    # suite.addTest(TestLogin('test_follow_user'))
    # suite.addTest(TestLogin('test_unfollow_user'))
    # suite.addTest(TestLogin('test_post_comment'))
    # suite.addTest(TestLogin('test_like_post'))
    # suite.addTest(TestLogin('test_unlike_post'))
    # suite.addTest(TestLogin('test_update_profile_picture'))
    # suite.addTest(TestLogin('test_update_bio'))
    # suite.addTest(TestLogin('test_update_website'))
    # suite.addTest(TestLogin('test_view_story'))
    # suite.addTest(TestLogin('test_send_message'))
    # suite.addTest(TestLogin('test_view_followers'))
    # suite.addTest(TestLogin('test_view_following'))
    suite.addTest(TestLogin('test_search_user'))
    # suite.addTest(TestLogin('test_block_user'))
    
    runner = unittest.TextTestRunner(resultclass=CustomTestResult)
    runner.run(suite)
