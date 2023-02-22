#%%
from project import*

while(True):
    print('*'*20)
    print("쇼핑몰 검색순위 분석")
    print('*'*20)
    print("1) 3일간 최대 많이 나온 검색어 상위 20") #완
    print("2) ") 
    print("3) 검색어 순위 워드 클라우드") #진행중
    print("4) 검색어 순위 막대 그래프") # 완
    print("5) 상품 검색 후 브랜드 워드클라우드") #진행중
    print("6) 상품 검색 후 브랜드 원 그래프") #완
    print("7) ")
    print("8) ")
    print("9) ")
    print("0) 종료")
    in_num=int(input("보고싶은 메뉴의 번호를 입력하세요.\n"))


    
    if(in_num==1):
        search_top(file_to_counter())

    elif(in_num==2):
        raise Exception('구현 미완성')

    elif(in_num==3):
        # 검색어 순위 워드 클라우드
        raise Exception('워드 클라우드 미완성')

    elif(in_num==4):
            # 검색어 순위 막대 그래프
        show_bar(file_to_counter())
        

    elif(in_num==5):
            # 상품 검색 후 브랜드 리스트 출력
            # 함수
        print()
        

    elif(in_num==6):
        # 상품 검색 후 원 그래프
        brand_circle()
        print('이미지 저장?')
        s=input('y/n')
        if(s=='y' or s=='Y'):
            raise Exception('저장 기능 미완성')
            
        else:
            raise Exception('그냥 미완성')
        
        
    elif(in_num==7):
        print('7번 실행')
        


    elif(in_num==8):
        print('8번 실행')

    elif(in_num==9):
        raise Exception('구현 미완성')

    elif(in_num==0):
        print('프로그램을 종료합니다.')
        break

    else:
        print("올바르지 않은 입력입니다.")
# %%
