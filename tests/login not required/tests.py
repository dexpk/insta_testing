import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class TestInstagramNoLogin(unittest.TestCase):
    
    def setUp(self):
        #Add Path to your chromedriver
        chrome_driver_path = 'C:/Users/verma/OneDrive/Desktop/Projects/selenium/drivers/chromedriver.exe'
        chrome_options = Options()
        chrome_options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        service = Service(chrome_driver_path)
        
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.instagram.com/")
    
    def test_homepage_elements(self):
        """Test that key elements are present on the homepage."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Instagram']")))
            self.assertTrue(self.driver.find_element(By.XPATH, "//a[text()='Instagram']").is_displayed())
            self.assertTrue(self.driver.find_element(By.XPATH, "//p[contains(text(),'Don’t have an account?')]").is_displayed())
        except TimeoutException:
            self.fail("Homepage key elements not found.")
    
    def test_footer_links(self):
        """Test that footer links are present and navigate correctly."""
        footer_links = {
            "About Us": "about",
            "Support": "help",
            "Press": "press",
            "API": "developer",
            "Jobs": "about/jobs",
            "Privacy": "legal/privacy",
            "Terms": "legal/terms"
        }
        for link_text, partial_url in footer_links.items():
            try:
                link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                link.click()
                WebDriverWait(self.driver, 10).until(EC.url_contains(partial_url))
                self.driver.back()
            except TimeoutException:
                self.fail(f"Footer link '{link_text}' did not navigate correctly.")
    
    def test_search_functionality(self):
        """Test that the search bar is functional."""
        try:
            search_bar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
            self.assertTrue(search_bar.is_displayed())
            search_bar.send_keys("test")
            suggestions = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'fuqBx')]")))
            self.assertTrue(suggestions.is_displayed())
        except TimeoutException:
            self.fail("Search functionality is not working.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
