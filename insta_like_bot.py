from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import getpass

class InstaLikeBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = input("Enter Username: ")
        self.password = getpass.getpass()
    
    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        time.sleep(2)

    def like_posts(self):
        html = self.driver.find_element_by_tag_name('html')
        while True:
            button=self.driver.find_element_by_css_selector("[aria-label='Like'][height='24']")
            time.sleep(0.5)
            button.click()
            html.send_keys(Keys.DOWN)
            time.sleep(3)
            
    def like_posts_in_a_profile(self):
        #This is like all the posts in a profile.

        search_box = self.driver.find_element_by_css_selector("[placeholder='Search']")
        profile_name = input("Enter the profile name: ")
        search_box.send_keys(profile_name)
        time.sleep(1)
        search_box.send_keys(Keys.ENTER)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)
        self.scroll_to_bottom()
        time.sleep(2)
        html = self.driver.find_elements_by_tag_name('html')
        time.sleep(0.5)
        html[0].send_keys(Keys.HOME)
        time.sleep(1)
        self.driver.find_element_by_css_selector("div[class='v1Nh3 kIKUG  _bz0w']").click()
        time.sleep(1)
        try:
            unlike_button = self.driver.find_element_by_css_selector("[aria-label='Unlike'][height='24']")
        except:
            button=self.driver.find_element_by_css_selector("[aria-label='Like'][height='24']")
            time.sleep(0.5)
            button.click()
        while(True):
            photo = self.driver.find_elements_by_css_selector("a[class=' _65Bje  coreSpriteRightPaginationArrow']")
            if photo:
                photo[0].click()
                time.sleep(2)
                try:
                    unlike_button = self.driver.find_element_by_css_selector("[aria-label='Unlike'][height='24']")
                except:
                    button=self.driver.find_element_by_css_selector("[aria-label='Like'][height='24']")
                    time.sleep(0.5)
                    button.click()
            else:
                break

    def scroll_to_bottom(self):
        SCROLL_PAUSE_TIME = 1.5
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

Instabot = InstaLikeBot()
Instabot.login()
# Instabot.like_posts()
# Instabot.like_posts_in_a_profile()