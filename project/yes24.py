import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import seaborn as sns

# [판다스 불러오기]
df = pd.read_csv('./python/project/data/data_out.csv')
print( df.head() )              # 상위 5개 출력하여 데이터 확인
df.info()                       # 속성 타입 확인
print( df.isnull().sum() )      # 결측치 확인


# [데이터 전처리]

#  1. 가격 데이터 전처리
#     가. 쉼표(,) 제거 및 "원" 문자열 제거
df['가격'] = df['가격'].str.replace(',', '').str.replace('원', '')

#     나. 숫자형(int) 변환, 예시: "18,500원" → 18500
df['가격'] = pd.to_numeric( df['가격'] , errors='coerce' ).fillna(0)

# 확인 : 
print( df['가격'] )


#  2. 출판년월 데이터 전처리
print( df['출판년월'] )
#     가. 연도(year) 컬럼 추출
df['연도'] = df['출판년월'].str.slice(0,4)
print( df['연도'])

#     나. 월(month) 컬럼 추출,
df['월'] = df['출판년월'].str.slice(6,8)
print( df['월'] )



# 3. 기본 통계 분석 기능
#   1. 가격 통계 분석
#     가. 평균 가격 계산
average_price = df['가격'].mean()
print( "평균 가격 계산 : " , average_price )

#     나. 최고 가격 계산
high_price = df['가격'].max()
print( "최고 가격 계산 : " , high_price )

#     다. 최저 가격 계산
low_price = df['가격'].min()
print( "최저 가격 계산 : " , low_price )

#   2. 출판년도 분석
#     가. 연도별 도서 수 계산
year_book = df['연도'].value_counts().sort_index()
print( year_book )

# 4. 데이터 시각화 기능
#   1. 가격 분포 시각화
#     가. 히스토그램 구현
plt.hist( df['가격'] , color='yellow' , alpha = 0.5 , bins = 30 )
plt.title('가격별 책 분포 시각화 ')
plt.ylabel('(권)')
plt.xlabel('가격')
plt.show()

#     나. 가격대별 도서 개수 출력
price_bookcount = df['가격'].value_counts().sort_index()
print( price_bookcount )
#     다. 그래프 제목 및 축 이름 출력
# -


#   2. 출판년도별 도서 수 시각화
#     가. 막대그래프 구현
plt.figure(figsize=(10, 6)) # 그래프 크기 설정
year_book.plot(kind='bar', color='skyblue')
plt.xlabel('연도')
plt.ylabel('(권)')
plt.title('출판년도별 도서 수 시각화')
plt.show()
#     나. 연도별 출판 도서 수 출력
#     다. 그래프 제목 및 축 이름 출력
