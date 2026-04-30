
# p.164
# 파이썬 조건문 , if 조건 :

number = int(input('정수 입력 : '))

if number > 0 :
    print('양수입니다') # 자바와 다르게 들여쓰기를 이용하여 실행문을 구분한다.


if number < 0 :
    print('음수입니다.')

if number == 0 :
    print('0입니다.')



# p.178
# if ~ else
number = int(input("정수 입력:"))
if number % 2 == 0 :
    print("짝수")
else :
    print("홀수")

# if ~ elif ~ elif ~ else , java : else if
if number % 2 == 0 :
    print("짝수")
elif number % 2 == 1 :
    print("홀수")
else :
    print("잘못된 값")       

# 조건 3개 이상 : [1] if if [2] if ~ elif
    
