# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:11:29 2019

@author: sportykush
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Firefox()
username = "your username"
password = "your password"
    
def closeBrowser():
    driver.close()

driver.get("https://www.instagram.com/")
time.sleep(2)
login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
login_button.click()
time.sleep(2)
user_name_element = driver.find_element_by_xpath("//input[@name='username']")
user_name_element.clear()
user_name_element.send_keys(username)
password_element = driver.find_element_by_xpath("//input[@name='password']")
password_element.clear()  
password_element.send_keys(password)
password_element.send_keys(Keys.RETURN)
time.sleep(2)
    
# Like all the images that are loaded on login
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
for like_link in driver.find_elements_by_link_text('Like'):
    like_link.click()
hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
                'newyork', 'artsy', 'alumni', 'lion', 'best', 'fun', 'happy',
                'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
                'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
                'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce']
tag = random.choice(hashtags)

# Like all the images on a specific hashtag
driver.get("https://www.instagram.com/explore/tags/" + tag + "/")
time.sleep(2)

# gathering photos
pic_hrefs = []
for i in range(1, 7):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        # get tags
        hrefs_in_view = driver.find_elements_by_tag_name('a')
        # finding relevant hrefs
        hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                if '.com/p/' in elem.get_attribute('href')]
        # building list of unique photos
        [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
    except Exception:
     continue

# Liking photos
unique_photos = len(pic_hrefs)
for pic_href in pic_hrefs:
    driver.get(pic_href)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        time.sleep(random.randint(2, 4))
        like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
        like_button().click()
        for second in reversed(range(0, random.randint(18, 28))):
            print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
            time.sleep(1)
    except Exception as e:
        time.sleep(2)
    unique_photos -= 1
            
closeBrowser()