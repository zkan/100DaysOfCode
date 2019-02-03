import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


TWITTER_URL = 'http://www.twitter.com'
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')

driver = webdriver.Chrome()
driver.get(TWITTER_URL)

elem = driver.find_element_by_name('session[username_or_email]')
elem.send_keys('zkancs')
elem = driver.find_element_by_name('session[password]')
elem.send_keys(TWITTER_PASSWORD)
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_name('tweet')
elem.send_keys('Day 75: Tweeted by Selenium script #100DaysOfCode')

tweet_button = '//button[contains(@class, "tweet-action")]' \
    '/span[contains(@class, "tweeting-text")]'
driver.find_element_by_xpath(tweet_button).click()

driver.close()
