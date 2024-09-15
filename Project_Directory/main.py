from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import os
import time

internet_test_speed = InternetSpeedTwitterBot()
internet_test_speed.get_internet_speed()
internet_test_speed.twitter_bot()