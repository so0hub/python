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
with open(r'C:\Users\sku-102-09\Desktop\python\python\day08\아파트(매매)_실거래가_20260424164421.csv_20260424164423690_msedge.exe.csv', 'r') as file:
    contents = file.read()
print(contents)




# ========================================================================
# 파일에서 회원 정보 불러오기 함수

import os # 내 컴퓨터의 파일이나 폴더를 확인하는 도구
# 메모장(users.txt)에 저장된 글자들을 읽어서 파이썬 리스트로 만드는 함수
def load_users():
    # 만약 내 컴퓨터에 user.txt라는 파일이 존재하는지 확인하는 것임
    if os.path.exists("users.txt"):
        with open("users.txt","r",encoding='utf-8') as file: # 파일이 있으면 읽기모드 'r'로 파일을 연다.
            lines = file.readlines() # 파일 안에 있는 모든 줄을 한꺼번에 읽어서 리스트 형태로 가져옴

            loaded_list = [] # 읽어온 글자 데이터를 담을 빈 바구니(리스트)를 준비

            for line in lines: # 읽어온 문장들을 한 줄씩 꺼내서 확인함
                if line.strip():
                    loaded_list.append(eval(line.strip())) # eval : "글자"로 된 딕셔너리모양을 진짜 딕셔너리 객체로 변신시켜줌
                    # 예: "{'id': '1'}" (글자) -> {'id': '1'} (진짜 딕셔너리)
            return loaded_list # 다 담은 바구니를 함수 밖으로 보내주기
        
    else:
        print("회원 파일이 없어서 새로 생성합니다.")
        return []   # 아무것도 없으니 일단 빈 바구니를 돌려줌


# =========================================================================

# 식별번호 생성하기
import random
def get_rand_num():
    numbers = "0123456789"
    while(True):
        user_NO = "".join(random.sample(numbers,5))
        if(user_NO[0] not in '0'):
            break
    return user_NO
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


# =========================================================================

user_list = load_users()    # 프로그램 실행하자마자 위에서 만든 함수를 실행해 회원정보를 가져와 변수에 담음

# 만약 불러온 회원이 한 명도 없다면 그 때만 랜덤 유저를 만든다.
if not user_list:
    for i in range(10): # 10명의 가짜 유저 생성
        user_info = {
            "식별번호" : get_rand_num() ,
            "아이디" : get_rand_id() ,
            "비밀번호" : get_rand_pwd() ,
            "이름" : get_rand_name()
        }
        user_list.append(user_info)

    # 생성 후 파일에 한 번 저장해두기
    with open("users.txt","w",encoding='utf-8') as file:
        for user in user_list:
            file.write(str(user)+"\n")  # user_list는 리스트 객체이므로 str()로 감싸서 문자열로 바꿔야 write가 가능하다고 함




#       - 로그인
# 사용자에게 로그인 정보 입력받기
input_id = input("아이디를 입력해주세요.\n")
input_pwd = input("비밀번호를 입력해주세요.\n")
def login(id,pwd,data_list):
    # 회원목록 바구니에서 한 명씩 정보 꺼내봄
    for user in data_list:
        if user["아이디"] == id and user["비밀번호"] == pwd: 
            return user["이름"]
    return None
  
result_name = login(input_id,input_pwd,user_list) # 로그인 함수를 실행하고 그 결과를 변수에 저장함

if result_name:
    print(f"{result_name}님 환영합니다!")
else:
    print("정보가 일치하지 않습니다.")


