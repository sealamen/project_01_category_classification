from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox') # 특허시스템이나 가상환경일 경우. 회사에서는 꼭 쓰임
options.add_argument('--disable-dev-shm-usage') # 리눅스쓰면 필요(1)
options.add_argument('disable_gpu')             # 리눅스쓰면 필요(2)
driver = webdriver.Chrome('./chromedriver', options = options)


# url = 'https://klyrics.net/category/korean/'
# driver.get(url)
# driver.find_element_by_xpath(
#  '//*[@id="tdi_66"]/article[1]/div/div[2]/header/h2/a').click()
# title = driver.find_element_by_xpath('//*[@id="tdi_63"]/div/div/div/div[1]/div/p[1]').text
# print(title)
# driver.back()
# driver.find_element_by_xpath(
#     '//*[@id="tdi_66"]/article[2]/div/div[2]/header/h2/a').click()
# title2 = driver.find_element_by_xpath('//*[@id="tdi_66"]/article[1]/div/div[2]/header/h2/a').text
# print(title2)
# driver.back()

# '//*[@id="tdi_66"]/article[1]/div/div[2]/header/h2/a'
# '//*[@id="tdi_66"]/article[2]/div/div[2]/header/h2/a'


# 계속 이런 식으로 xpath를 따오고 드라이버백해서 나오고, 그러면 이 페이지에
# 있는 것들은 다 긁어올 수 있음. 다음 페이지로 가려면 페이지 주소를 봐봐.
# 유사성이 있으면 for문 돌리면 되겠지

url = 'https://www.naver.com/'
driver.get(url)
driver.find_element_by_xpath('//*[@id="account"]/a').click()
driver.find_element_by_xpath('//*[@id="id"]').send_keys('wltjrdlqns')
driver.find_element_by_xpath('//*[@id="pw"]').send_keys('********')
# 검사에 name이 있는 애들은 name으로 접근 가능.
# driver.find_element_by_name('id').send_keys('wltjrdlqns')
driver.find_element_by_xpath('//*[@id="log.login"]').click()