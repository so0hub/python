
import pandas as pd

# 서비스 클래스
class ItemService :
    def __init__(self):
        self.df = pd.DataFrame( [
            { 'id' : 1 , 'name' : '박진감' , 'price' : '???'} ,
            {  'id' : 2 , 'name' : '박소영' , 'price' : '???'}
            
        ] )
        # 함수
        # (1) 개별조회 서비스
    def item( self , id ) :
        # df[ 조건식 ]  # df[ df['특정열'] == 값 ]
        result = self.df[ self.df['id'] == id ] # 판다스에 있는 아이디가 입력받은 아이디와 같을 때
        if result.empty : # empty 비어있으면
            return "해당 상품이 없습니다."
        # df 타입 대신에 .to_json() 또는 .to_dict()
        print( result )  # df 조회 결과는 항상 리스트 형식
        return result.to_dict( orient = 'records' )

# ** 서비스 객체 생성 **
item_service = ItemService()