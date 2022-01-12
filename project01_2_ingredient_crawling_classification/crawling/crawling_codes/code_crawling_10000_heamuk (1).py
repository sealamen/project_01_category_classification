# -*- coding: utf-8 -*-
"""code_crawling_10000_heamuk.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pzgGMCMVNt7yzqzk7x9L6Oc0-4u6m9DE
"""

## 만개의 레시피 양식

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']


# 일단 90페이지까지
for i in range(1,90):
    url = 'https://www.10000recipe.com/recipe/list.html?cat4=65&order=reco&page={}'.format(i)
    for j in range(1, 41):
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="contents_area_full"]/ul/ul/li[{}]/div[1]/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                '//*[@id="divConfirmedMaterialArea"]/ul/a[{}]/li'.format(k)).text
                ingredient += ' ' + a
                ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
        except:
            ingredients.append(ingredient)
            ingredient = ''
            df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
            df_section_titles['Category'] = category[3]



df_section_titles.to_csv('./10000recipe_western.csv')
driver.close()

## 해먹남녀 한식

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from bs4 import BeautifulSoup

pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

ingredient = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']

for i in range(1,200):
    url = 'https://haemukja.com/recipes?category_group2%5B%5D=60&page={}'.format(i)
    driver.get(url)
    for j in range(1, 13):
        
        elem = driver.find_element_by_xpath('//*[@id="content"]/section/div[2]/div/ul/li[{}]/p/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                '/html/body/div/div[1]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[{}]/span'.format(k)).text
                ingredient.append(a)
        except:
            df_section_titles = pd.DataFrame(ingredient, columns=['Ingredient'])
            df_section_titles['Category'] = category[0]
            ingredient.clear()


df_section_titles.to_csv('./crawling/koreanfood.csv')
driver.close()

## 만개의 레시피 중식[키워드]


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']


url = 'https://www.10000recipe.com/recipe/list.html?q=%EC%82%AC%EC%B2%9C'
try:
    for j in range(1, 41):
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="contents_area_full"]/ul/ul/li[{}]/div[1]/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                '//*[@id="divConfirmedMaterialArea"]/ul/a[{}]/li'.format(k)).text
                ingredient += ' ' + a
                ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
        except:
            ingredients.append(ingredient)
            ingredient = ''
            df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
            df_section_titles['Category'] = category[2]
except:
    pass


df_section_titles.to_csv('./10000recipe_Sichuan_china.csv')
driver.close()

## 해먹남녀 한식

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re

pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']

for i in range(1,201):
    url = 'https://haemukja.com/recipes?category_group2%5B%5D=60&page={}'.format(i)
    for j in range(1, 13):
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="content"]/section/div[2]/div/ul/li[{}]/p/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                '/html/body/div/div[1]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[{}]/span'.format(k)).text
                ingredient += ' ' + a
                ingredient = re.compile('[^가-힣|a-z|A-Z ]').sub(' ', ingredient)
        except:
            ingredients.append(ingredient)
            ingredient = ''
            df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
            df_section_titles['Category'] = category[0]


df_section_titles.to_csv('./korean.csv')
driver.close()

## 10000개의 레시피 양식

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']

# 일단 90페이지까지
for i in range(37,90):
    url = 'https://www.10000recipe.com/recipe/list.html?cat4=65&order=reco&page={}'.format(i)
    for j in range(1, 41):
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="contents_area_full"]/ul/ul/li[{}]/div[1]/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                '//*[@id="divConfirmedMaterialArea"]/ul/a[{}]/li'.format(k)).text
                ingredient += ' ' + a
                ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
        except:
            ingredients.append(ingredient)
            ingredient = ''
            df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
            df_section_titles['Category'] = category[3]


df_section_titles.to_csv('./10000recipe_western137.csv')
driver.close()

## 시행착오

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from bs4 import BeautifulSoup

pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

url = 'https://haemukja.com/recipes?category_group2%5B%5D=60&page=1'
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')
soup.find()
print(soup)
    # for href in soup.find("div", class_="w_news_list").find_all("li"):
    #     print(href.find("a")["href"])


# .call_recipe.thmb.docs-creator (클래스명)

pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

url = 'https://haemukja.com/recipes?category_group2%5B%5D=60&page=1'
driver.get(url)
driver.find_element_by_link_text('recipes')

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from bs4 import BeautifulSoup

pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

url = 'https://haemukja.com/recipes?category_group2%5B%5D=60&page=1'
driver.get(url)

elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from bs4 import BeautifulSoup

pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

url = 'https://haemukja.com/recipes?category_group2%5B%5D=60&page=1'
driver.get(url)

elem = driver.find_element_by_xpath('//*[@id="content"]/section/div[2]/div/ul/li[1]/p/a')
elem.get_attribute("href")

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from bs4 import BeautifulSoup

pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}


url = 'https://haemukja.com/recipes/5977'
driver.get(url)
a = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[1]/span').text
print(a)

c = pd.read_csv('./koreanfood.csv')
c

## 해먹남녀 양식

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']
# 91
for i in range(1,91):
    url = 'https://haemukja.com/recipes?category_group2%5B%5D=87&page={}'.format(i)
    for j in range(1, 13):
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="content"]/section/div[2]/div/ul/li[{}]/p/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                '/html/body/div/div[1]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[{}]/span'.format(k)).text
                ingredient += ' ' + a
                ingredient = re.compile('[^가-힣|a-z|A-Z ]').sub(' ', ingredient)
        except:
            ingredients.append(ingredient)
            ingredient = ''
            df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
            df_section_titles['Category'] = category[3]


df_section_titles.to_csv('./Western.csv')
driver.close()

## 만개의 레시피(키워드 : 중국)


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']

# 12페이지
for i in range(1,13):
    url = 'https://www.10000recipe.com/recipe/list.html?q=%EC%A4%91%EA%B5%AD&order=reco&page={}'.format(i)
    for j in range(1, 41):
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="contents_area_full"]/ul/ul/li[{}]/div[1]/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                '//*[@id="divConfirmedMaterialArea"]/ul/a[{}]/li'.format(k)).text
                ingredient += ' ' + a
                ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
        except:
            ingredients.append(ingredient)
            ingredient = ''
            df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
            df_section_titles['Category'] = category[2]


df_section_titles.to_csv('./Chinese.csv')
driver.close()

# url = 'https://www.10000recipe.com/recipe/list.html?q=%EC%A4%91%EA%B5%AD&order=reco&page={}'.format(i)

# /html/body/dl/dd/ul/ul/li[2]/div[1]/a

# //*[@id="contents_area_full"]/ul/ul/li[1]/div[1]/a 
# //*[@id="contents_area_full"]/ul/ul/li[1]/div[1]/a
# //*[@id="contents_area_full"]/ul/ul/li[2]/div[1]/a
# //*[@id="contents_area_full"]/ul/ul/li[15]/div[1]/a

# //*[@id="contents_area_full"]/ul/ul/li[22]/div[1]/a
# //*[@id="contents_area_full"]/ul/ul/li[23]/div[1]/a
# //*[@id="contents_area_full"]/ul/ul/li[40]/div[1]/a

df_section_titles.to_csv('./Chinese.csv')

# 만개의 레시피(키워드 : 중식)


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']

# 3

for i in range(1,3):
    url = 'https://www.10000recipe.com/recipe/list.html?q=%EC%A4%91%EC%8B%9D&order=reco&page={}'.format(i)
    try:
        for j in range(1, 41):
            driver.get(url)
            elem = driver.find_element_by_xpath('//*[@id="contents_area_full"]/ul/ul/li[{}]/div[1]/a'.format(j))
            new_url = elem.get_attribute("href")
            driver.get(new_url)
            try:
                for k in range(1, 40):
                    a = driver.find_element_by_xpath(
                    '//*[@id="divConfirmedMaterialArea"]/ul/a[{}]/li'.format(k)).text
                    ingredient += ' ' + a
                    ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
            except:
                ingredients.append(ingredient)
                ingredient = ''
                df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
                df_section_titles['Category'] = category[2]
    except:
        break


df_section_titles.to_csv('./Chinese2.csv')
driver.close()

## 만개의 레시피 키워드 일식

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']

# 4페이지까지

for i in range(1,5):
    url = 'https://www.10000recipe.com/recipe/list.html?q=%EC%9D%BC%EC%8B%9D&order=reco&page={}'.format(i)
    try:
        for j in range(1, 41):
            driver.get(url)
            elem = driver.find_element_by_xpath('//*[@id="contents_area_full"]/ul/ul/li[{}]/div[1]/a'.format(j))
            new_url = elem.get_attribute("href")
            driver.get(new_url)
            try:
                for k in range(1, 40):
                    a = driver.find_element_by_xpath(
                    '//*[@id="divConfirmedMaterialArea"]/ul/a[{}]/li'.format(k)).text
                    ingredient += ' ' + a
                    ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
            except:
                ingredients.append(ingredient)
                ingredient = ''
                df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
                df_section_titles['Category'] = category[1]
    except:
        break


df_section_titles.to_csv('./japanese_keys_jw.csv')
driver.close()

## 만개의 레시피 키워드 일본

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']

# 13페이지까지

for i in range(9,14):
    url = 'https://www.10000recipe.com/recipe/list.html?q=%EC%9D%BC%EB%B3%B8&order=reco&page={}'.format(i)
    try:
        for j in range(1, 41):
            driver.get(url)
            elem = driver.find_element_by_xpath('//*[@id="contents_area_full"]/ul/ul/li[{}]/div[1]/a'.format(j))
            new_url = elem.get_attribute("href")
            driver.get(new_url)
            try:
                for k in range(1, 40):
                    a = driver.find_element_by_xpath(
                    '//*[@id="divConfirmedMaterialArea"]/ul/a[{}]/li'.format(k)).text
                    ingredient += ' ' + a
                    ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
            except:
                ingredients.append(ingredient)
                ingredient = ''
                df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
                df_section_titles['Category'] = category[1]
    except:
        break


df_section_titles.to_csv('./japanese_keys_jp3.csv')
driver.close()

## 만개의 레시피 키워드 일본

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']

# 13페이지까지

for i in range(1,14):
    url = 'https://www.10000recipe.com/recipe/list.html?q=%EC%9D%BC%EB%B3%B8&order=reco&page={}'.format(i)
    for j in range(1, 41):
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="contents_area_full"]/ul/ul/li[{}]/div[1]/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                '//*[@id="divConfirmedMaterialArea"]/ul/a[{}]/li'.format(k)).text
                ingredient += ' ' + a
                ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
        except:
            ingredients.append(ingredient)
            ingredient = ''
            df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
            df_section_titles['Category'] = category[1]



df_section_titles.to_csv('./japanese_keys_jp.csv')
driver.close()

df

df_section_titles.to_csv('./10000recipe_western_asp.csv')

df_section_titles