# [ Python Practice7 종합예제]

# 경기도 아파트 실거래가 조회 시스템 ( 리스트와 딕셔너리 사용 )
# 데이터 출처: 국토교통부 실거래가 공개시스템(경기도 최근 1년치 아파트 매매 데이터) 
# https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=

# 주요 기능 요구사항
# 1. 데이터 저장 및 로드 (파일 처리)
#     users.txt: 회원 정보 저장 (식별번호,아이디,비밀번호,이름) 직접 생성 
#     아파트(매매)_실거래가_20260424091956.csv: 직접 다운로드한 실거래가 데이터 파일

# 2. 사용자 기능 (로그인 후 이용 가능)
#     2-1) 공통 : 
#       - 회원가입, 
#       - 로그인
#       - 로그아웃
#     2-2) 회원 전용 메뉴: ( 어려운분들은 구현 안해도 됩니다. )
#       - 지역명 검색: '시군구' 열에서 사용자가 입력한 지역명(예: "만안구", "평촌동")이 포함된 모든 거래 내역 출력
#       - 금액 범위 검색: 사용자가 입력한 '최소 금액'과 '최대 금액' 사이의 거래 내역 필터링 출력
#       - 전체 통계 조회: 전체 데이터의 평균 거래가 등 간단한 통계 정보 출력


# CSV 파일 읽기 헐 
with open('./python/day08/아파트(매매)_실거래가_20260424164421.csv', 'r') as file:
    contents = file.read()
print(contents)


# 회원 정보 저장
# 식별번호 생성하기
import random
def get_rand_num():
    numbers = [0,1,2,3,4,5,6,7,8,9]

    number = random.choice(numbers)
    return number
print(get_rand_num())


# 아이디 생성하기
import random
def get_rand_id():
    ids = "abcdefghizklmnopqrstuvwxyz0123456789"
    while(True):
        user_ID = "".join(random.sample(ids,8))
        if(user_ID[0] not in '0123456789'): # 첫 번째 자리에는 숫자가 못 들어가도록
            break
    return user_ID
print(get_rand_id())


# 비밀번호 생성하기
import random
def get_rand_pwd():
    pwds = "abcdefghizklmnopqrstuvwxyz0123456789!~*@"
    while(True):
        user_PWD = "".join(random.sample(pwds,8))
        if(user_PWD[0] not in '0123456789!~*@'):
            break
    return user_PWD
print(get_rand_pwd())


# 이름 생성하기
import random
def get_rand_name():
    last_names = ["김","이","박","최","남궁","제갈","최"]
    first_names = ["진","감","소","영","란","희","승","권","주","련"]

    last_name = random.choice(last_names) # Last name 생성
    first_name = "".join(random.sample(first_names,2)) # First name 생성
    full_name = last_name + first_name # Full name 생성
    
    return full_name
print(get_rand_name())


# 사용자 정보 생성 및 저장
# 10명의 랜덤 유저 정보를 생성해 리스트에 담기
user_list = []


for i in range(10): # 10명의 가짜 유저 생성
    user_info = {
        "number" : get_rand_num() ,
        "id" : get_rand_id() ,
        "pwd" : get_rand_pwd() ,
        "name" : get_rand_name()
    }
    user_list.append(user_info)

# 파일 쓰기
with open("users.txt","w",encoding='utf-8') as file:
    for user in user_list:
        file.write(str(user)+"\n")  # user_list는 리스트 객체이므로 str()로 감싸서 문자열로 바꿔야 write가 가능하다고 함
print("users.txt 저장 완료")


# 2. 사용자 기능 (로그인 후 이용 가능)
#     2-1) 공통 : 
#       - 회원가입,
 
#       - 로그인
#       - 로그아웃