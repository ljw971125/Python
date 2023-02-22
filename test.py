#%%
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from collections import Counter #가운트 
import matplotlib.pyplot as plt
import platform

def brand_circle():
        li=[]
        for i in range(1,11): # 첫페이지 부터 10페이지 까지 수집
                url = Request('https://www.musinsa.com/categories/item/018003?d_cat_cd=018003&brand=&list_kind=small&sort=sale_high&sub_sort=1y&page='+str(i)+'&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=', headers={'User-Agent': 'Mozilla/5.0'})
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
        low_value = []
        low_label=[]

        imsi=[]

        for i in range(len(labels)):
    
                if(values[i] <= 20):
                        low_value.append(values[i])
                        low_label.append(labels[i])
                else:
                        high_value.append(values[i])
                        high_label.append(labels[i])
        
      
        plt.pie(high_value, labels=high_label, explode=[0, 0.1, 0, 0, 0, 0, 0, 0], autopct='%.2f')
        plt.show