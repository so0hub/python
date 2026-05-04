
# pip install matplotlib


# [1] 맷프롭릿 설치 : pip install matplotlib
# [2] 맷플롭릿 import matplotlib
import matplotlib as mpl
print( mpl.__version__ )    # 3.10.9


# [*] 한글 지원 안 됨
import matplotlib as mpl
mpl.rc('font', family='Malgun Gothic') # 또는 'Noto Sans CJK JP'
mpl.rcParams['axes.unicode_minus'] = False




# [1] 선 그래프 , 데이터의 추세(변화) , .plot()
import matplotlib.pyplot as plt
# 1. 그래프의 데이터 준비
x = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]   # x축( 가로축의 값 )
y = [ 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0 ]   # y축( 세로축의 값 )

# 2. 그래프 설정
plt.plot( x , y )               # .plot( x값 , y값 )
plt.title( 'Line Chart Title' )  # .title('차트제목')
plt.xlabel( 'X-axis Title' )   # .xlable( 'x축제목' )
plt.ylabel( 'Y-axis Title' )   # .ylable( 'y축제목' )
plt.grid(True)
                 # .grid(True) , 눈금선 표시
# 3. 그래프 출력
plt.show()

# [2] 선 그래프2
y2 = [0,1,2,3,4,5,6,7,8,9]
plt.plot( x , y , label = '감소하는 선(항목명)' , color = 'blue' , linestyle = ':' )
plt.plot( x , y2 , label = '증가하는 선(항목명)' , color = 'red' , linestyle = '-' )

plt.legend()        # 범례에 항목명 표시

plt.show()

# [3] 막대 그래프 , 데이터의 비교 , .bar( x축값 , y축값 , width = 굵기 , label = '항목명' , color = '색상' )
categories = [ '학생1' , '학생2' , '학생3' , '학생4' ]
values = [ 85, 92, 78, 90 ]
values2 = [ 85 , 91 , 75 , 85]

# 막대 겹치지 않게 표시 , width = '막대굵기' , *인덱스(위치번호)를 활용한 크기 조정
import numpy as np
x = np.arange( len(categories) )   # 0부터 x축의 값 개수 만큼 생성 , 0 ~ 3  

plt.bar( x - 0.2 , values , width=0.4 , label = '국어성적' , color = 'blue' )
plt.bar( x + 0.2 , values2 , width=0.4 , label = '수학성적' , color = 'aqua' )
plt.title( '학생 성적 비교')
plt.xlabel('학생명')
plt.ylabel('성적점수')
plt.legend()
plt.grid( axis='y') # 눈금선 ( y축만 )
plt.xticks( x , categories )    # 위치(0~3) 순으로 라벨( 학생1 ~ 학생4 ) 지정

plt.show()


# [4] 파이 그래프 , 백분율 , .pie()
labels = [ '피자' , '햄스터' , '박진감' , '마라씨양궈' ]
sizes = [ 40 , 30 , 20 , 10 ]
colors = [ 'aqua' , '#ffa8ee' , '#b6ddf7' , 'lightgreen' ]
explode = [ 0.1 , 0 , 0 , 0]    # 원형에서 튀어나오는 정도(강조)

plt.pie( sizes , labels=labels , colors=colors , explode=explode , startangle=90 , autopct='%1.0f%%' )
# %형식문자 %자릿수.소수자릿수f , f실수 ,  %% : 형식문자가 아닌 '%' 표시
plt.title( '음식 선호도')
plt.legend()
plt.show()

# [5] 선점도 , 밀집도 , .scatter( x축값 , y축값 , c(color) = '색상' , s = 점크기  )
x = [ 1.5 , 2.5 , 3.5 , 4.5 , 5.5 ]
y = [ 50,60,65,70,75 ]
plt.scatter( x , y , c = 'red' , s = 100 )
plt.grid()
plt.show()

# [6] 히스토그램 , 상관관계 , .hist( 값 , color='' , alpha= 투명도 , bins= 구간개수 )
# 샘플 데이터
data = []
for i in range( 500 ) : # 500번 반복
    value = sum( [ ( i * j ) % 100 / 100 for j in range( 1 , 13 ) ] )    # 리스트 내포 ( 1차원 리스트 생성 )
    # ( i * j ) % 100 : 나머지값 계산
    # /100 : 0~1 사이 값으로 계산
    # sum( ) : 총합계 , 즉] 13개의 0 ~ 1 사이의 난수를 만들어서
    data.append( value )
    print( data )
# 차트 만들기
plt.hist( data , color='yellow' , alpha= 0.5 , bins= 30)
plt.show()

# [7] 다중 그래프 표현 , .subplots( 행 , 열 )
fig , axs = plt.subplots( 1 , 2 , figsize=( 10 , 7 ) )    # 한 줄에 2개 차트

# fig : 다중 그래프를 가지고 있는 전체 그래프
# axs : 다중 그래프의 위치 , axs[0] 첫번째 그래프 , axs[1] 두번째 그래프
# figsize = ( 가로 , 세로 ) , 전체 그래프의 가로inch / 세로inch
axs[0].plot( [1,2,3],[1,4,9] )
axs[0].set_title('선그래프')        # 주의할점 : .title( )  전체 그래프의 제목 , .set_title( ) 하위 그래프의 제목
axs[0].set_xlabel('x축제목')        # 즉] .title , xlabel 등 에서는 set_XXXX( ) 으로 사용하기.
axs[0].set_ylabel('y축제목')
axs[1].bar( [1,2,3] , [3,5,2] )
axs[1].set_title('막대그래프')
axs[1].set_xlabel('x축제목')
axs[1].set_ylabel('y축제목')

# plt.savefig('저장경로')   # 그래프 이미지( png )  다운로드
plt.savefig('./day13/save_chart.png')  
plt.show()


# fig , axs = plt.subplots( 2 , 2 )     # 행 = 2 , 열 = 2 , 총 그래프수 = 4
# axs[0][0].plot()
# axs[0][1].bar()
# axs[1][0].scatter()
# axs[1][1].pie()