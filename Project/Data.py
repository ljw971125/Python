# 전체 검색 순위(20개 화면에 표시하기)
# 1번함수
def imsi_file():
    lis22=[]
    f=open('search_ranking_name.txt','r',encoding='utf-8')
    for i in f.readlines():
        lis22.append(i)
    f.close()

    cnt=0
    print()
    #print(str(lis22).replace("'",'').replace('[','').replace(']','').replace(',',""))
    for i in range(len(lis22)):
        print(str(lis22[i]).replace('\n',' '),end='\t')
        cnt+=1
        if(cnt%5==0):
            print()
    print()