from selenium import webdriver
from credentials import username, password
import time
from selenium.webdriver.common.keys import Keys

class InstaLikeBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        time.sleep(2)

    def like_posts(self):
        html = self.driver.find_element_by_tag_name('html')
        while True:
            button=self.driver.find_element_by_css_selector("svg[aria-label='Like'][height=24]")
            time.sleep(0.5)
            button.click()
            html.send_keys(Keys.DOWN)
            if input() == 0:
                break

Instabot = InstaLikeBot()
Instabot.login()
# Instabot.like_posts()