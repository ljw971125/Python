def search_data():
    import csv
    import requests
    from bs4 import BeautifulSoup

    name=input("검색할 것을 입력해주세요.\n")
    request=requests.get('https://www.musinsa.com/search/musinsa/goods?q='+name+'&list_kind=small&sortCode=sale_high&sub_sort=1y&page=1&display_cnt=0&saleGoods=false&includeSoldOut=false&setupGoods=false&popular=false&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=&serviceType=&eventType=&type=popular&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=false&d_cat_cd=&attribute=')
    html_data=request.text
    soup=BeautifulSoup(html_data,"html.parser")

    keyword_list=[]
    result=soup.find_all('div',class_='list_img')

    for i in result:
        keyword_list.append(i.find('a')['data-bh-content-nm'])
    
    for j in keyword_list[:5]:
        print(j)