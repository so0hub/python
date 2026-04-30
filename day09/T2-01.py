# T2-01.py
# (1) numpy 이란 ? 고성능 수치 계산 라이브러리
# (2) 설치 : 터미널에서 'pip install numpy'
# (3) numpy 불러오기 : import numpy
# (4) numpy 버전 확인하기
import numpy
print( numpy.__version__ )  # 버전 확인 : 2.4.4


# [1] 넘파이 배열 생성
x = [1,2,3,4]   # 일반 리스트
print( x )

x = numpy.array( [1,2,3,4] )    # .array( 자료 )    # 넘파이는 리스트라 안 하고 배열이라 함. ([1차원리스트])
print( x ) # [1 2 3 4]  # 쉼표가 따로 안 나옴 넘파이

x = numpy.array( [ [1,2,3] , [4,5,6] ] )    # .array( [ [1차원리스트],[1차원리스트] ] )   # 2차원 리스트
print( x ) # [[1 2 3]
           # [4 5 6]]  # 출력하면 두 줄로 나옴

# .zeros( (행,열) ) , 행 과 열 만큼의 0으로 초기화
x = numpy.zeros( (2,3) )   
print( x )  
# [[0. 0. 0.]
# [0. 0. 0.]]

# .ones( (행,열) ) , 행 과 열 만큼의 1 으로 배열 초기화
x = numpy.ones( (2,3) )  
print( x )
# [[1. 1. 1.]
# [1. 1. 1.]]

#  .full( ( 행,열 ) , 값 ) , 행 과 열 만큼의 값으로 배열 초기화
x = numpy.full( (2,3) , 10 )    
print( x )
# [[10 10 10]
#  [10 10 10]]


# .arrange( 시작값 , 끝값, 단위) , 시작 부터 끝 사이의 단위만큼 증가한 배열 
x = numpy.arange( 0,10,2 )
print( x )  # [0 2 4 6 8]

# .linspace( 시작 , 끝 , 개수 ) , 시작 부터 끝 사이의 개수만큼 균등하게 나눈 배열
x = numpy.linspace( 0,1,5 )
print( x )  # [0.   0.25 0.5  0.75 1.  ]