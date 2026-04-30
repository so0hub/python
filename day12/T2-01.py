
# numpy : 배열 기반 , 공학 수치 계산에 용이함
# pandas : 테이블 기반 , 전처리/필터링(numpy)

# [1] pandas 설치 : pip install pandas
# [2] import pandas as pd
import pandas as pd # 변수명 아무거나 , 주로 pd를 많이 씀
print( pd.__version__ ) # 3.0.2

# series
# 1. 생성
x = [ 10, 20, 30, 40 ]  # 리스트
z = pd.Series( x )
print( z )

# 0    10        # 0 ~ 4 : 각 요소들의 인덱스
# 1    20        # 10 ~ 50 : 각 요소의 값
# 2    30
# 3    40
# dtype: int64   # 데이터의 타입

# 2. 각 요소들의 라벨 포함하기
y = [ 'a', 'b', 'c', 'd' ]
z = pd.Series( x , index=y )    # index에 라벨(목록) 대입
print( z )
# a    10           # a ~ d : 각 요소들의 인덱스(라벨)
# b    20           # 10 ~ 50 : 각 요소의 값
# c    30
# d    40
# dtype: int64

# 3. 딕셔너리 으로 생성
# 파이썬 주요 타입 , [리스트] (튜플) {딕셔너리}
x = { 'apple' : 1 , 'parkjingam' : 2 , 'parskoyoung' : 3 }
z = pd.Series( x )
print( z )
# apple          1
# parkjingam     2
# parskoyoung    3
# dtype: int64

# 4. 주요 속성 확인
print( z.dtype )    # 타입 반환     ,   int64
print( z.index )    # 인덱스 반환   ,   Index(['apple', 'parkjingam', 'parskoyoung'], dtype='str')
print( z.values )   # 값반환    ,   [1 2 3]
print( z.head() )   # .head(n)  ,   상위 n개(기본값:5)개만 출력 ( 확인용 )
# apple          1
# parkjingam     2
# parskoyoung    3
# dtype: int64
print( z.tail )     # .tail(n)  ,   하위 n개만 출력
# <bound method NDFrame.tail of 
# apple          1
# parkjingam     2
# parskoyoung    3
# dtype: int64>

# 5. 인덱싱 , 슬라이싱
print( z.iloc[0] )  # .lioc[인덱스번호]  ,  라벨이 아닌 위치로 조회   # 1
print( z.iloc[:] )  # apple          1
                    # parkjingam     2
                    # parskoyoung    3
                    # dtype: int64
print( z.loc['parkjingam'] )                # .loc[ 라벨명 ]    ,   라벨명으로조회
print( z.loc['apple' : 'parkjingam'] )      # .loc[ 시작라벨 : 끝라벨 ]

# 6. 데이터 수정
z['apple'] = 10     # [ 라벨명 ] = 새로운값
print( z )
print( z['apple'] ) # 10

# 7. 데이터 추가
z[ 'berray' ] = 40
print( z )

# 8. 병합   , .concat( [ x , y ] )
# 판다스 합치기
x = pd.Series( [10,20,30] , index=['a','b','c'] )
y = pd.Series( [40,50] , index=['d','e'] )
z = pd.concat( [ x , y ] )
print( z )
# a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int64


# 9. 라벨 이름 변경 , .rename( { '기존라벨' : '새로운라벨' } )
x = z.rename( {'a' : 'apple'} )
print( x )

## [참고] 파이썬 , 문자(리터럴)
test = 'hello java'             # hello java
test = test.replace(' ','-')    # 공백을 -로 변경   # 문자열(리터럴)은 불변성이 특징.
print( test )                   # hello-java



# 10. 필터링 , [ 조건식 ] , [ ( 조건식1) | (조건식2) ]
print( z[ z > 30 ] )        # 30 초과 필터링

x = z[ z > 30 ]
print( x )

x = z[ ( z < 25 ) | ( z > 35 ) ]    # 25보다 작거나 35보다 크다
print( x )

x = z[ ( z > 25 ) & ( z < 35 ) ]    # 25보다 크면서 35보다 작다
print( x )

z[ z > 30 ] = z[ z > 30 ] + 10  # 30 초과한 요소값에 10 더한 후에 30 초과한 요소에만 대입
print( z )


# 11. 통계
print( z.sum() )                            # .sum() 합계
print( z.mean() )                           # .mean() 평균
print( z.max() )                            # .max() 최댓값
print( z.min() )                            # .min() 최솟값
print( z.median() )                         # .median() 중앙값
print( z.var() )                            # .var() 분산
print( z.std() )                            # .std() 표준편차
print( z.count() )                          # .count() 요소 개수
print( z.value_counts() )                   # .value_counts() 각 요소별 중복 개수
print( z.value_counts( normalize=True ) )   # .value_counts( normalize=True )   각 요소가 전체에서 차지하는 비율(0~1)


# 12. 정렬  ,  한 쪽이 정렬되면 다른 쪽이 같이 이동된다.
# 오름차순 :  .sort_index()  ,   .sort_values()   
# 내림차순 :  .sort_index( ascending= False )   , .sort_values( ascending= False )
x = z.sort_index()                        # 인덱스(라벨) 기준으로 정렬(asc)
print( x )
x = z.sort_values()                       # 값 기준의 정렬(asc)
print( x )

x = z.sort_index( ascending= False )      # 내림차순(desc)
print( x )
x = z.sort_values( ascending= False )     # 내림차순(desc)
print( x )

# 13. 그룹
# .groubby( level = 0 ).집계함수() , 그룹 이후에 집계 중요
# .groubby( level = 0 ).agg( ['함수명' , '함수명'] )
z = pd.Series( [10,20,30,10,20,30] ,
    index = ['a','b','a','b','a','b'] )

x = z.groupby( level=0 ).sum()             # 인덱스(라벨)별 총합계
print( x )

x = z.groupby( level=0 ).mean()            # 인덱스(라벨)별 평균
print( x )

x = z.groupby( level=0 ).agg( [ 'sum' , 'mean' , 'count' ] )   # 여러개 집계함수는 agg 함수로 묶어서 표현 
print( x )

