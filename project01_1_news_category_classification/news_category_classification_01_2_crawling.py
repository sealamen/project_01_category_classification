from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time

def crawl_title():
    try:
        title = driver.find_element_by_xpath('//*[@id="section_body"]/ul[{1}]/li[{0}]/dl/dt[2]/a'.format(i, j)).text
        title = re.compile('[^가-힣a-zA-Z]').sub(' ', title)
        print(title)
        titles.append(title)
    except NoSuchElementException:
        title = driver.find_element_by_xpath('//*[@id="section_body"]/ul[{1}]/li[{0}]/dl/dt/a'.format(i, j)).text
        title = re.compile('[^가-힣a-zA-Z]').sub(' ', title)
        print(title)
        titles.append(title)

    # 그림이 없는 경우에 번호가 안잡히는 경우가 있어(except문의 링크처럼)
    # 그럴 경우 에러가 떠서 문제가 발생할 수 있으니 try except문 사용

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox') # 특허시스템이나 가상환경일 경우. 회사에서는 꼭 쓰임
options.add_argument('--disable-dev-shm-usage') # 리눅스쓰면 필요(1)
options.add_argument('disable_gpu')             # 리눅스쓰면 필요(2)

# 한글 쓴다고 설정잡아준 것

driver = webdriver.Chrome('./chromedriver', options = options)
# driver가 크롬 드라이버를 운전할 운전수를 하나 만든거야

# 이제 뉴스를 크로울링할 것. 정치부터
# xpath 보면 다음과 같음. 이중포문 돌리자
# //*[@id="section_body"]/ul[1]/li[1]/dl/dt[2]/a
# //*[@id="section_body"]/ul[1]/li[2]/dl/dt[2]/a
# //*[@id="section_body"]/ul[1]/li[5]/dl/dt[2]/a
# //*[@id="section_body"]/ul[2]/li[1]/dl/dt[2]/a
# //*[@id="section_body"]/ul[3]/li[1]/dl/dt[2]/a
# //*[@id="section_body"]/ul[4]/li[5]/dl/dt[2]/a

df_titles = pd.DataFrame()
pages = [131,131,131,101,131,77]
# 다중분류기는 크기가 비슷비슷해야하므로, 131에 맞추자
category = ['Politics', 'Economics', 'Social', 'Culture', 'World', 'IT']

for l in [2,3]:   # 섹션을 바꾸는 포문. 100~105
    titles = []
    for k in range(1,pages[l]):  # 페이지를 바꾸는 포문. 주소 끝 page=
        url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}#&date=%2000:00:00&page={}'.format(l,k)
        driver.get(url)
        # time.sleep(1)  # 로드되는 시간 사이에 오류가 날 수 있으므로 그동안 sleep을 줌
        for j in range(1,5):
            for i in range(1,6):
                try:
                    crawl_title()
                except StaleElementReferenceException:
                    driver.get(url)
                    print('StaleElementReferenceException')
                    time.sleep(1)
                    crawl_title()
                # 위에서 timesleep 주는 대신에 이렇게 써주면 더 빠르지
                # 페이지가 빨리 안바뀌어서 발생하는 에러
                # 얘는 시간이 부족해서 나타나는 error니까 위에 했던 걸로 크로울링을 다시 하면 돼.
                # 시간을 멈췄다가 다시 크로울링하게끔 했어
                # 대신에 코드 재사용성이 떨어지니까 함수 써버리자
                except:
                    print('error')
                # 그 이외에 지정되지 않은 에러들은 이리로와.

        if k % 50 == 0: # 50개씩 나눠서 저장하자
            df_section_titles = pd.DataFrame(titles, columns=['title'])
            df_section_titles['category'] = category[l]
            df_section_titles.to_csv('./crawling/news_{}_{}--{}'.format(category[l], k-49, k),
                                     index=False)
            titles = []
            # for 문 안에서 k로 50나눴을 때 0일때마다 한 번씩 저장하기
            # clear를 한 번 해줘야함
    df_section_titles = pd.DataFrame(titles, columns=['title'])
    df_section_titles['category'] = category[l]
    df_section_titles.to_csv('./crawling/news_{}_remain.csv'.format(category[1]),
                             index=False)
    # for문 나와서도 한 번 저장

df_titles.to_csv('./crawling/naver_news.csv')
print(len(titles))
driver.close()

# 페이지정보가 없이 가면 1페이지로 가는 거고, 페이지 2를 갔다가 오면
# 페이지정보가 있는 url이 나타남. 우리는 for문 돌릴거니까 페이지정보 있게
# format함수 쓸 때 format(i,j)를 주면 앞에 {} 안에 0을 준 데에 i, 1을 준 데에 j가 옴
# 20개 중에 지금 빈 게 있다면(에러가 나도)실행될 수 있도록 try except를 주자
# 2 5가 없다고 나오는데, 이런 경우 dt뒤에 숫자가 없음. 그 이유는 이미지가 없어서
# 그럼 except문에다가 dt[] 부분에 [] 빼고 주도록 해버리면 돼.

# 저장을 하는데 하다가 오류가 나버리면 저장 안돼. 그러니 다 나눠서 저장해주자.
# 그리고 그것들을 추후에 다 더하는 방식으로!