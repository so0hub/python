# p. 326

# 콜백함수 : 함수의 매개변수에 사용하는 함수
def call_10_items( func ) : # 매개변수로 받는 함수
    for i in range( 10 ) :
        func()

def print_hello():
    print("안녕하세요")

call_10_items( print_hello )        # 함수자체
# call_10_items( print_hello() )      # 함수실행 () 소괄호

# map() , filter() 함수
# map( 함수 , 리스트 ) : 리스트의 요소를 * 하나씩 * 함수매개변수에 대입하여 * 새로운 리스트 * 반환
# filter( 함수 , 리스트 ) : 리스트의 요소를 * 하나씩 * 함수매개변수에 대입하여 참(True)인 경우 * 새로운 리스트 * 반환

def power( item ) :
    return item * item

def under_3( item ) :
    return item < 3     # 3 미만 True 반환

list_input_a = [ 1, 2, 3, 4, 5 ]    #

# JAVA 였다면 : list_input_a.stream.map( 함수 ).toList()        # 함수 vs  () -> {}
# JS 였다면 : list_input_a.map( 함수 )                          # 함수 vs  () -> {}
# PY : map(함수,list_input_a)

output_a = map( power , list_input_a )
print( list( output_a ) )                   # [1, 4, 9, 16, 25]

output_b = filter( under_3 , list_input_a )
print( list(output_b) )                     # [1, 2]

# 제너레이터 : 함수 내부에 yield 키워드를 사용하며 next()함수를 외부에서 호출하여 yield 키워드까지 실행한다.
def test() : 
    print("A 지점 통과")
    yield 1
    print( "B 지점 통과")
    yield 2

test()                  # 함수 호출시 실행이 안 된다.
output = test()         # (1) 함수 반환값을 변수에 저장
a = next( output )      # (2) 함수 반환값이 저장된 변수를 next에 대입한다.    # A 지점 통과
print( a )              # (3) yield 까지 실행되고 yield 반환값이 반환된다.

b = next( output )      # B 지점 통과
print( b )              # 2

# c = next( output )      # 다음 yield 가 없으므로 예외 발생
# print( c )

# 람다 : 함수 선언 간단하게 하는 문법
# lamda 매개변수 : 반환값

# JS 방법 1 : JS 선언적함수 콜백
# function 함수명(){}       , const 변수명 = () => {}
# <button onClick = { 함수명 }>

# JS 방법 2 : JS 람다(화살표) 콜백
# <button onClick = { () => {} }>

# 방법1 : 재사용 가능하다.
power = lambda x : x * x
output_a = map( power , list_input_a )
# 방법2 : 재사용 안 된다.
output_a = map( lambda x : x * x , list_input_a )


# 파일 처리
# open( 파일경로 , 읽기모드 ) , file 객체가 반환된다.
# 읽기모드 : w새로쓰기 a이어쓰기 r읽기모드

# (1) open 함수 이용하여 지정한 경로의 파일 쓰기
file = open('./day06/basic.txt','w')  # 현재 .py 파일 폴더내 basic.txt 생성

# (2) .write( 출력할내용 ) 함수 이용한 내보내기
file.write( '안녕하신감 박진감..!' )

# (3) .close() 함수 이용한 안전하게 스트림 닫기
file.close()

# (4) with 키워드 이용한 .close() 자동 닫기
with open( './day06/basic2.txt' , 'w' ) as file :
    file.write('안녕하신감 박진감2..!')

# 스트림이란? 데이터가 흐르는 길 , 바이트단위 , 프로그래밍언어가 외부 자료와 연결(파일,JDBC,네트워크 등)

# (5) .read() 함수 이용한 파일 읽어오기
with open('./day06/basic.txt','r') as file :
    contents = file.read()
print( contents )       # 안녕하신감 박진감..!


import random
hanguls = list("가나다라마바사아자차카타파하")
with open("info.txt","w") as file :
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
        
        file.write("{},{},{}\n".format(name,weight,height))


with open("info.txt","r") as file:
    for line in file:
        (name,weight,height) = line.strip().split(",")

        if(not name) or (not weight) or (not height):
            continue
        bmi = int(weight) / ((int(height)/100)**2)
        result = ""
        if 25 <= bmi :
            result = "과체중"
        elif 18.5 <= bmi :
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름:{}",
            "몸무게:{}",
            "키:{}",
            "BMI:{}",
            "결과:{}"
        ]).format(name,weight,height,bmi,result))
        print()

# p. 352
# 마무리 문제1
numbers = [1,2,3,4,5,6]
print("::".join(str(s) for s in numbers))



# 마무리 문제2
numbers = list(range(1,10+1))
print('#홀수만 추출하기')
print(list(filter(lambda i : i%2 != 0, numbers)))
print()

print('# 3 이상, 7 미만 추출하기')
print(list(filter(lambda i : 3<=i<7,numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda i : i ** 2 < 50 ,numbers)))
print()