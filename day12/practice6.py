import pandas as pd
print( pd.__version__ )
# 문제 1: 인덱스 불일치와 결측치 처리

# 딕셔너리 데이터 sales = {'mon': 100, 'tue': 200, 'wed': 300}를 Series로 변환하되, 
# 인덱스를 ['월', '화', '수']로 지정하여 생성하고 그 결과를 출력하시오. 
# (발생하는 현상과 이유를 주석으로 설명하시오.)
sales = {'mon': 100, 'tue': 200, 'wed': 300}
x = pd.Series( sales )
print( x )
x = x.rename( {'mon':'월','tue':'화','wed':'수'} ) # 인덱스 변경하는 코드
print( x )


# 문제 2: 슬라이싱을 이용한 부분 수정
# data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])에 대하여
data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
# 1. iloc을 사용하여 인덱스 'b'부터 'd'까지의 값을 추출하고 기존 값에 2를 곱하여 수정하시오.
data.iloc[1:4] = data.iloc[1:4] * 2
print( data )


# 2. loc을 사용하여 인덱스 'd'의 값을 100으로 변경한 뒤 전체를 출력하시오.
data.loc['d'] = 100
print( data )

# 문제 3: Series 연결과 중복 인덱스 조회
# s1 = pd.Series([1, 2], index=['a', 'b'])와  s1 = pd.Series([1, 2], index=['a', 'b'])를 
s1 = pd.Series([1, 2], index=['a', 'b'])
s2 = pd.Series([1, 2], index=['a', 'b'])
# pd.concat을 사용하여 연결(result)하고, 인덱스 'a'를 loc으로 조회했을 때의 결과를 출력하시오.
result = pd.concat([s1,s2])
print( result['a'] )
# a 1
# a 1


# 문제 4: 복합 조건을 활용한 데이터 변경
# data = pd.Series([15, 25, 35, 45, 55])에서 값이 30보다 크고 50보다 작은 요소들만 
# 필터링하여 기존 값에 5를 더한 뒤, 최종 배열의 상태를 출력하시오.
data = pd.Series([15, 25, 35, 45, 55])
x = data[ ( data > 30 ) & ( data < 50 ) ] + 5
print( x )


# 문제 5: 범주형 데이터의 빈도수 및 비율 분석
# grade = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B']) 데이터에 대하여
grade = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B'])
# 1. 각 알파벳별 빈도수(value_counts)를 출력하시오.
print( grade.value_counts() )

# 2. 각 알파벳이 차지하는 상대적 비율을 소수점 형태로 출력하시오. (normalize 인자 활용)
print( grade.value_counts( normalize=True) )

# 문제 6: 산술 연산에서의 인덱스 정렬(Alignment)
# s1 = pd.Series([10, 20], index=['a', 'b'])와 s2 = pd.Series([30, 40], index=['b', 'c'])가 있을 때,
# 두 Series를 더한(s1 + s2) 결과를 출력하고 결측치(NaN)가 발생한 위치와 이유를 설명하시오.
s1 = pd.Series([10, 20], index=['a', 'b'])
s2 = pd.Series([30, 40], index=['b', 'c'])
result = s1 + s2
print( result )
# a     NaN 
# b    50.0
# c     NaN
# dtype: float64
# 발생한 위치 : a , c   /  발생한 이유 : a,c는 짝이 없음

# 문제 7: 다중 정렬 구현 (Values & Index)                                                        **********************
# data = pd.Series([20, 10, 20, 30], index=['d', 'c', 'a', 'b'])에 대하여
# 데이터 값(Values)은 내림차순으로 정렬하고, 값이 같을 경우 인덱스(Index)를 
# 오름차순으로 정렬한 최종 결과를 출력하시오.
data = pd.Series([20, 10, 20, 30], index=['d', 'c', 'a', 'b'])

# 1차 정렬 이후에 유지하기 위해서 , 1차 정렬에 kind 속성에 'stable' 적용하여 유지할 수 있다.
# sort(2차정렬).sort(1차정렬)
result3 = data.sort_index().sort_values( ascending=False , kind='stable' )
print( result3 )


# 정렬 따로 하는 경우에는 1차 정렬과 2차 정렬 유지 불가능
result = data.sort_values( ascending=False ) 
result2 = result.sort_index()
print( result2 )   



# 문제 8: 그룹화 및 다중 집계 함수 적용
# data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'A', 'B']) 데이터를 
# 인덱스 레벨(level=0) 기준으로 그룹화하여, 합계(sum)와 평균(mean)을 동시에 구하고 출력하시오.
data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'A', 'B'])
x = data.groupby(level=0).agg( [ 'sum' , 'mean' ] )
print( x )

# 문제 9: 가중 평균(Weighted Average) 계산
# 과목별 점수 score = pd.Series([80, 90, 70], index=['math', 'eng', 'sci'])와 
# 가중치 weight = pd.Series([0.4, 0.3, 0.3], index=['math', 'eng', 'sci'])를 활용하여
# 각 과목의 가중 점수를 합산한 최종 총점을 브로드캐스팅 연산을 통해 구하시오.
# ***** 가중치 : 각 항목이 전체 결과에서 차지하는 비중
# ***** [점수 x 비중]을 먼저 해서 각 과목의 '실제반영점수'를 계산해야 함
score = pd.Series([80, 90, 70], index=['math', 'eng', 'sci'])
weight = pd.Series([0.4, 0.3, 0.3], index=['math', 'eng', 'sci'])
x = ( score * weight ).sum()
print( x )

# 문제 10: 필터링 및 인덱스 재설정 (Reset Index)                                                   **********************
# data = pd.Series([10, 30, 20, 40], index=['a', 'b', 'c', 'd'])에서 
data = pd.Series([10, 30, 20, 40], index=['a', 'b', 'c', 'd'])
# 1. 값이 25보다 큰 데이터만 추출하여 새로운 Series를 만드시오.
x = data[ data > 25 ] 
print( x )
# 2. 추출된 Series의 기존 문자 인덱스를 제거하고 0부터 시작하는 숫자 인덱스로 재설정하시오.
y = x.reset_index( drop = True )
print( y )