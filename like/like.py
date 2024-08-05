from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/verma/OneDrive/Desktop/Projects/insta_testing/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.instagram.com/")
time.sleep(10)

username = driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[1]/div/label/input")

username.send_keys("automationinsta1")

password = driver.find_element("xpath", "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[2]/div/label/input")

password.send_keys("870945@Piyush")

password.send_keys(Keys.ENTER)
time.sleep(10)

driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[2]/div[2]/span/div").click()
time.sleep(10)

search = driver.find_element("xpath", "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")

search.send_keys("cristiano")
time.sleep(10)

driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]").click()
time.sleep(10)

post = driver.find_element("xpath", "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div[1]/div[1]/a/div[1]/div[2]")

post.click()
time.sleep(10)
try:
    like = driver.find_element("xpath","/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div")

    like.click()
    time.sleep(10)
except Exception:
    input("Press Enter to close the browser...")
    driver.quit()

input("Press Enter to close the browser...")
driver.quit()

