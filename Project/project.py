#!/usr/bin/env python
# coding: utf-8

# In[1]:
from collections import Counter
import requests
from bs4 import BeautifulSoup
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep #sleep함수
from collections import Counter #카운트
from urllib.request import urlopen,Request
import matplotlib.pyplot as plt
import platform

# In[1]:
# 3일간 최대 많이 나온 검색어 상위 20
def search_top(cnt):
    import operator
    string_list=list(cnt.keys()) # 읽어온 카운터의 키값(상품명)을 리스트로 저장
    int_list=list(cnt.values()) # 읽어온 카운터의 value값(빈도수)를 리스트로 저장

    dic = { x:y for x,y in zip(string_list,int_list) } # 두 개의 리스트를 딕셔너리화 (중복제거 x)
    sorted_by_value = sorted(dic.items(), key=operator.itemgetter(1), reverse=True) # value(빈도수)값으로 내림차순 정렬
    for i in range(0,20,2):
        print("%10s \t %10s\n"%(sorted_by_value[i][0],sorted_by_value[i+1][0]))


# In[2]:
# 저장된 파일을 바탕으로 막대그래프
def show_bar(counter):
    if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
    elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
    elif platform.system() == 'Linux': #리눅스 (구글 콜랩)

        plt.rc('font', family='Malgun Gothic') 
    plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결
    
    labels=list(counter.keys())
    values=list(counter.values())
    plt.figure(figsize=(20,10))
    plt.title("3일간의 검색 빈도수")
    plt.xlabel("검색어")
    plt.ylabel("빈도수")
    # for i in range(20):
    #     plt.bar(labels[i],values[i])
    plt.bar(labels[:20],values[:20])

def file_to_counter():  
    f=open('save2_data.txt','r',encoding='utf-8') # 축적된 파일 열기
    lis=[] # 데이터를 읽어서 저장할 임시 리스트
    lis.append(f.read()) # 임시 리스트에 데이터를 읽어서 저장
    f.close() # 파일닫기
    
    lis2=[] # 임시 저장용 리스트
    for i in lis: # 파일에서 읽어서 저장한 리스트를 읽기
        lis2.append(i.split('\n')) #  \n 을 구분으로 임시 저장용 리스트에 저장
    lis.clear() # 리스트 클리어
    for i in lis2[0]: # 위의 split으로 2차원 배열이 되었음
        lis.append(i) # 비워둔 리스트에 붙이기
    lis=list(filter(len,lis))  # 빈 공백문자열을 filter로 제거
    
    cnt=Counter(lis) # 리스트를 카운트화
    print()
    return cnt
       

# 1 검색어 순위 데이터 20등 까지 수집하는 함수
def get_ranklist():
    # 모듈 불러오기
    
    # 임시 리스트 생성
    li=[]
    li2=[]
    # url불러오기
    url="https://www.musinsa.com/ranking/keyword"
    request=requests.get(url)
    html_data=request.text
    soup=BeautifulSoup(html_data,"html.parser")
    
    # 20등 까지의 검색어 순위 리스트 생성
    
    len_cnt=0
    for f_text in soup.find_all("li"):
        li.append(f_text.a['title'])
    for i in range(20):
        li2.append(li[i])
    print(li2)
    return li2




# 저장된 파일을 바탕으로 워드클라우드



# In[5]:


# 2 키워드별 판매순으로 브랜드 카운팅
# 상품 검색후 브랜드 카운팅
def search_brand():    
    input_product = input('상품명을 입력해주세요.') # 상품명 입력
    
    driver=webdriver.Chrome("C:\chromedriver\chromedriver.exe") #크롬드라이버
    driver.get("https://www.musinsa.com/app/") 
    
    # 크롬 드라이버 동작 부분
    driver.find_element(By.XPATH,'//*[@id="search_query"]').click()
    sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="search_query"]').send_keys(input_product)
    sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="search_button"]').click()
    sleep(0.1)
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/section/div[3]/div/section[1]/header/a/h2').click()
    sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="goodsList"]/div[1]/a[7]/span').click()
    sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="layerSorting_sale"]/div/label[5]').click()
    sleep(0.1)

    URL=driver.current_url
    test_Url=URL.split('page')



    brand_li=[] #브랜드 리스트
    for i in range(1,11): # 첫페이지 부터 10페이지 까지 수집
        url = Request(test_Url[0]+'page='+str(i)+test_Url[1][2:], headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        brand_name=soup.find_all('p',class_="item_title")
        
        for j in range(len(brand_name)):
            brand_li.append(brand_name[j].text)
        
    brand_counter = Counter(brand_li)
    return brand_counter


# In[ ]:


# 카운팅된 브랜드, 숫자 파일로 저장 


# In[ ]:


# 브랜드파일 워드클라우드


# In[6]:


# 브랜드 파일 원그래프
def brand_circle():
        if platform.system() == 'Darwin': #맥
                plt.rc('font', family='AppleGothic') 
        elif platform.system() == 'Windows': #윈도우
                plt.rc('font', family='Malgun Gothic') 
        elif platform.system() == 'Linux': #리눅스 (구글 콜랩)

                plt.rc('font', family='Malgun Gothic') 
                plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결

        counter = search_brand()

        labels=list(counter.keys())
        values=list(counter.values())

        high_value = []
        high_label=[]
        
        for i in range(len(labels)):
                if(values[i] >= 20):
                        high_value.append(values[i])
                        high_label.append(labels[i])
        
        explode_max = 0
        explode_value = []

        for i in range(len(high_value)):
                if high_value[i] > explode_max:
                        explode_max = high_value[i]
        
        for i in range(len(high_value)):
                if high_value[i] == explode_max:
                        explode_value.append(0.1)
                else:
                        explode_value.append(0)
        
      
        plt.pie(high_value, labels=high_label, explode=explode_value, autopct='%.2f')
        plt.show


# In[ ]:


# 프로그램 실행 함수



# %%
