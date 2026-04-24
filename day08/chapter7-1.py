
# OS 모듈
# p. 410

import os                   # os 모듈 호출
print( os.name )            # nt : 윈도우 뜻
print( os.getcwd() )        # 현재 최상위 폴더
print( os.listdir() )       # 현재 최상위 폴더의 내부 요소

os.mkdir('hellogam')        # 폴더 생성됨
os.rmdir('hellogam')        # 폴더 삭제됨

with open('./day08/original.txt','w') as file :
    file.write('hellogam')

os.rename('./day08/original.txt' , './day08/new.txt')       # 파일명 변경

os.remove('./day08/new.txt')    # 파일 삭제
os.system('dir')                # 시스템 명령어 실행        # 보안 문제 주의!

# dateitem 모듈
import datetime

print( datetime.datetime.now() )
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 형식 : Y년 m월 d일 H시 M분 S초
output_a = now.strftime('%Y - %m - %d %H : %M : %S')   # 형식 만들기
print(output_a)

# p.413
# 시간 계산
output = now.replace( year=( now.year + 1 ) , month=( now.month - 1 ) )
print(output)

# time 모듈
import time
print('3초간 일시정지합니감')
time.sleep(3)           # 3초 간 일시정지   # 스레드 일시정지   # 스레드란? 코드가 실행되는 흐름단위
print('땡감')

# urllib 모듈
from urllib import request     # from 이용한 특정한 함수/변수 만 가져오기

target = request.urlopen( "https://google.com" )
output = target.read()
print(output)



# p.420
# 3번 문제
import os   # 모듈 읽어 들이기
# 폴더를 읽어 들이는 함수
def read_folder(path):
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path)
    #  폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(path+"/"+item):
             # 폴더라면 계속 읽어 들이기
            read_folder(path+"/"+item)
        else:
             # 파일이라면 출력하기
            print("파일:", item)
# 현재 폴더의 파일/폴더를 출력합니다.
read_folder(".")