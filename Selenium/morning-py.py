from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
import datetime

driver = webdriver.Chrome()
driver.get('https://weixin.sogou.com/')

wait = WebDriverWait(driver, 10)
input = wait.until(EC.presence_of_element_located((By.NAME, 'query')))
input.send_keys('早起Python')
driver.find_element_by_xpath("//input[@class='swz']").click()