from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver',options=options)


category = ['Korean', 'Japaness', 'Chinese', 'Western',]
df = pd.DataFrame(columns=['ingredients', 'category'])


url = 'https://www.serveq.co.kr/recipe/CHN/recipe_list'
driver.get(url)
for j in range(1, 8):
    for i in range(1, 13):
        try :
            driver.find_element_by_xpath('//*[@id="contents"]/section/div[2]/div/ul/li[{}]/a'.format(i)).click()
            rec_url = driver.current_url
            dfs = pd.read_html(rec_url)
            if '재료명' in dfs[0].columns :

                df.loc[(i + (j - 1) * 12) - 1] = [' '.join(dfs[0]['재료명']), category[2]]
            elif '원료명' in dfs[0].columns:
                df.loc[(i + (j - 1) * 12) - 1] = [' '.join(dfs[0]['원료명']), category[2]]
            driver.back()

        except:
            print('error')
            pass
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="contents"]/section/div[2]/div/div/span/a[{}]'.format(j)).click()


print(df)

df.to_csv('./crawling/serveq_chinese.csv', index = False)
