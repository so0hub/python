import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import urllib3

# [1] 크롤링 주소 확인 : https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber=42&pageSize=24
# # url = 'https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber=42'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
book_list=[]
# [2]
# 1~42페이지 크롤링
for page in range( 1, 43 ) :
    url = f'https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={page}'
    
    # [3] url 요청
    response = requests.get( url, verify=False, timeout=5 )

    # [4] 요청한 URL 의 성공했을 때 HTML로 파싱
    soup = BeautifulSoup( response.text , 'html.parser' )

    # [5] 가져올 식별자 , soup.select() : 여러개선택 , soup.select_one() : 하나선택
    books = soup.select( '#yesBestList > li' )
    for book in books :
        # 가. 도서 제목
        gd_name = book.select_one('.gd_name').get_text().strip()
        # 나. 가격
        yes_b = book.select_one('.yes_b').get_text().strip()
        # 다. 판매지수 saleNum
        saleNum = book.select_one('.saleNum').get_text().strip()
        # 라. 출판년월
        authPub_info_date = book.select_one('.authPub.info_date').get_text().strip()

        # [6] 리스트[]에 딕셔너리{} 포함하기
        book_list.append( { "제목" : gd_name , "가격" : yes_b , "판매지수" : saleNum , "출판년월" : authPub_info_date } )

    # [7] import time , time.sleep(초) , 지정한 초 만큼 코드(스레드)가 대기상태 , 즉] 요청 서버 과부하 방지
    time.sleep( 0.5 )

    # [8] 판다스에 넣어주기
    print( book_list )
    df = pd.DataFrame( book_list )
    print( df )

# [*] 판다스 자료 외부파일 내보내기
# .csv 내보내기
df.to_csv(
    'data_out.csv',                        # 파일경로
    index=False,                                   # 인덱스 불포함
    encoding='utf-8',                              # 인코딩 지정
    na_rep='Unknown',                              # 결측값 치환
    header=True                                    # 헤더(열이름) 포함여부
)