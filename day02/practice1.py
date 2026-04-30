# [ Python practice1 ]

# [ 단 ] if(제어문), for(반복문)은 사용하지 않습니다.

# [ 제출방법 ] 코드가 작성된 파일이 위치한 깃허브 상세 주소를 제출하시오.

# 문제 1: 원의 넓이 계산 반지름을 input()으로 입력받아 원의 넓이를 계산하여 출력하시오. (원주율은 3.14로 계산)
str_input = input("원의 반지름을 입력하세요 > ")
num_input = float(str_input)
print()
print("반지름 : ",num_input)
print("둘레 : ",2*3.14*num_input)
print("넓이 : ",3.14*num_input**2)

# 문제 2: 평균 점수 계산기 국어, 영어, 수학 세 과목의 점수를 각각 입력받아 총점과 평균을 구하여 출력하시오.
kor = float(input("국어 점수를 입력하세요 > "))
eng = float(input("영어 점수를 입력하세요 > "))
math = float(input("수학 점수를 입력하세요 > "))
total = kor + eng + math 
avg = total / 3

print("총점:",total)
print("평균",avg)

# 문제 3: 나머지 연산 활용 정수 하나를 입력받아 그 수가 짝수이면 0, 홀수이면 1이 출력되도록 작성하시오.
num = int(input("정수를 입력하세요 > "))
result = num % 2
print("결과 : " , result)

# 문제 4: 거듭제곱 계산 숫자 하나를 입력받아 해당 숫자의 제곱과 세제곱 값을 각각 출력하시오.
num =  int(input(" 거듭제곱 계산 숫자를 하나 입력하세요 > "))

result1 = num**2
result2 = num**3
print("해당 숫자의 제곱:",result1)
print("해당 숫자의 세제곱:",result2)


# 문제 5: 복합 대입 연산자 실습 변수 balance에 5000을 저장한 후, 복합 대입 연산자만을 사용하여 2000을 더하고, 다시 1500을 뺀 최종 값을 출력하시오.
balance = 5000
balance += 2000 
balance-= 1500
print("최종 값 : " ,balance)

# 문제 6: 문자열 길이 출력 사용자의 영문 이름을 입력받아 "당신의 이름은 [숫자]글자입니다."라고 출력하시오.
name = str(input(" 이름을 입력하세요 > "))
print("당신의 이름은",len(name),"글자 입니다.")

# 문제 7: 성과 이름 분리 "홍 길동"과 같이 공백이 포함된 이름을 입력받아, 인덱싱과 슬라이싱을 사용하여 성(첫 글자)만 출력하시오.d
name = str(input("이름을 입력하세요(ex:홍 길동)) > "))
print(name[0])

# 문제 8: 문자열 "Python"이 저장된 변수에서 콜론 하나(:)를 사용하는 슬라이싱을 통해 "Pyth"까지만 추출하여 출력하시오.
result = "Python"
print(result[0:4])

# 문제 10: 문자열 곱셈 연산 사용자로부터 문자열 하나와 숫자 하나를 입력받아, 해당 문자열을 숫자만큼 반복하여 출력하시오.
result_str = str(input("문자열을 입력하세요 > "))
result_int = int(input("숫자를 입력하세요 > "))

print(result_str * result_int)


# 문제 11: 정수형 변환 실수 3.9를 변수에 저장하고, 이를 정수형으로 변환하여 출력했을 때 소수점이 사라지는 것을 확인하시오.
num = float(3.9)
int(num)

# 문제 12: 두 수의 문자열 결합 두 개의 숫자를 입력받되, 계산이 아닌 문자열로 결합하여 출력하시오. (예: 10과 20 입력 시 1020 출력)
num1 = input("첫 번째 숫자를 입력하세요 > ")
num2 = input("두 번째 숫자를 입력하세요 > ")
print(num1+num2)

# 문제 13: 자동 형변환 확인 정수 10을 실수 2.0으로 나눈 결과를 출력하고, 해당 결과의 데이터 타입이 무엇인지 출력하시오.
a = int(10)
b = float(2.0)
print(type(a/b))

# 문제 14: 초를 분/초로 환산 전체 초(second)를 입력받아 몇 분 몇 초인지 계산하여 출력하시오. (예: 70초 -> 1분 10초)
result = int(input("전체 초(second)를 입력하세요"))
print( result // 60,"분",result % 60,"초" )