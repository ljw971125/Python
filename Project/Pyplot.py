#%%
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from collections import Counter #가운트 
import matplotlib.pyplot as plt
import platform

def brand_circle():
        li=[]
        name=input("검색할 것을 입력해주세요.\n")
        for i in range(1,11): # 첫페이지 부터 10페이지 까지 수집
                url = Request('https://www.musinsa.com/search/musinsa/goods?q='+name+'&list_kind=small&sortCode=sale_high&sub_sort=1y&page='+str(i)+'&display_cnt=0&saleGoods=false&includeSoldOut=false&setupGoods=false&popular=false&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=&serviceType=&eventType=&type=popular&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=false&d_cat_cd=&attribute=', headers={'User-Agent': 'Mozilla/5.0'})
                html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')

        brand_name=soup.find_all('p',class_="item_title")
        for j in range(len(brand_name)):
                li.append(brand_name[j].text)

        if platform.system() == 'Darwin': #맥
                plt.rc('font', family='AppleGothic') 
        elif platform.system() == 'Windows': #윈도우
                plt.rc('font', family='Malgun Gothic') 
        elif platform.system() == 'Linux': #리눅스 (구글 콜랩)

                plt.rc('font', family='Malgun Gothic') 
                plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결

        counter = Counter(li)

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
brand_circle()
# %%
