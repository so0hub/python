import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# [1] 크롤링 주소 확인 : https://www.yes24.com/product/category/bestseller?categoryNumber=001
# url = 'https://www.yes24.com/product/category/bestseller?pageNumber=001'

book_list=[]
# [2] 주소의 매개변수 분석 , categoryNumber=001&pageNumber=1&pageSize=24&age=20&sex=M
# 1~3페이지 크롤링 예
for page in range( 1 , 4 ) : # range( 시작 , 끝전까지 )
    url = f'https://www.yes24.com/product/category/bestseller?pageNumber={page}'
    # f'문자열{변수/계산식}문자열{변수/계산식}'
        
    # [3] url 요청
    response = requests.get( url )

    # [4] 요청한 URL 의 성공했을 때 HTML로 파싱
    soup = BeautifulSoup( response.text , 'html.parser' )

    # [5] 가져올 식별자 , soup.select() : 여러개선택 , soup.select_one() : 하나선택
    books = soup.select( '#yesBestList > li')
    # 책 여러개 : #yesBestList 여러개책정보 , li(책하나) 
    # 책 하나당 : ( .gd_name 제목 , .yes_b 가격 , .info_auth 저자 정보 )
    for book in books : # <li> 여러개이므로 반복문 가능
        # .strip() 앞뒤 공백 제거 , .split( 기준문자 ) 기준문자 기준으로 분리 , replace()
        gd_name = book.select_one('.gd_name').get_text().strip()
        yes_b = book.select_one('.yes_b').get_text().strip()
        info_auth = book.select_one('.info_auth').get_text().strip().replace( '\n' , '' )
    # [6] 리스트[]에 딕셔너리{} 포함하기
    book_list.append( { "제목" : gd_name , "가격" : yes_b , "저자정보" : info_auth } )
    # 자바 : add , 자바스크립트 : push , 파이썬 : append

    # [7] import time , time.sleep(초) , 지정한 초 만큼 코드(스레드)가 대기상태 , 즉] 요청 서버 과부하 방지
    time.sleep( 2 ) # 2초

    # [8] 판다스에 넣어주기
    print( book_list )
    df = pd.DataFrame( book_list )
    print( df )
    