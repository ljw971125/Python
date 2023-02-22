#%%
# 상품 검색후 브랜드 카운팅
def search_brand(product):
    import requests
    from selenium import webdriver
    from selenium.webdriver.common.by import By 
    from time import sleep #sleep함수
    from bs4 import BeautifulSoup
    from collections import Counter #카운트 
    from urllib.request import Request,urlopen

    driver=webdriver.Chrome("C:\chromedriver\chromedriver.exe") #크롬드라이버
    driver.get("https://www.musinsa.com/app/") 

    driver.find_element(By.XPATH,'//*[@id="search_query"]').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="search_query"]').send_keys(product)
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="search_button"]').click()
    sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/section/div[3]/div/section[1]/header/a/h2').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="goodsList"]/div[1]/a[7]/span').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="layerSorting_sale"]/div/label[5]').click()
    sleep(1)

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
search_brand('백팩')
# %%
