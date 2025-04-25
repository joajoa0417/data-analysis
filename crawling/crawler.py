from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Chrome() # 웹 창 생성
driver.maximize_window() # 웹 창 최대화
driver.get('https://shopping.naver.com/home') # 특정 url 웹사이트 이동
driver.implicitly_wait(1) # 정보를 받아오는 시간

path = '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div[1]/form/div/div/div/div/input' #XPATH는 도달하기까지의 경로를 의미
search_word = '모자'

search_box = driver.find_element(By.XPATH, path) # 변수 내에서 설정한 path 내에 XPATH가 있음을 의미
search_box.clear() # 창 비워줌(예외 처리)   
search_box.send_keys(search_word) # 검색어 입력
search_box.send_keys(Keys.ENTER) # 검색 실행

# last_height = driver.execute_script("return document.body.scrollHeight") # 스크롤 내리고 높이 측정

# for _ in range(10):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 스크롤 내리기
#     time.sleep(1) # 스크롤 내리고 1초 대기
#     new_height = driver.execute_script("return document.body.scrollHeight") # 스크롤 내리고 높이 측정
    
#     print(_)
#     # if new_height == last_height: # 스크롤 내리고 높이가 변화가 없으면 멈춤
#     #     break
    
#     # last_height = new_height # 스크롤 내리고 높이가 변화가 있으면 높이 저장
# print(driver.page_source)

items_path = '//*[@id="composite-card-list"]/div/ul[1]/li'
items = driver.find_elements(By.XPATH, items_path)


contents = items[3].find_element(By.CSS_SELECTOR, 'div > a').get_attribute('data-shp-contents-dtl')
cont_dic = json.loads(contents)

for cont in cont_dic:
    if cont['key'] == 'prod_nm':
        print(cont['value'])
    
    # print(cont, type(cont))


