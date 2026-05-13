# import pandas as pd
# #   3. 응답 예시
# # {   "평균가격": 17200,
# #     "최고가격": 45000,
# #     "최저가격": 5900,
# #     "최다출판연도": 2024  }
# class BookService :
#     def __init__(self):
#         self.df = pd.read_csv('./data/data_out.csv')
#         # 쉼표(,) 제거 및 "원" 문자열 제거
#         self.df['가격'] = self.df['가격'].str.replace(',', '').str.replace('원', '')

#         # 숫자형(int) 변환, 예시: "18,500원" → 18500
#         self.df['가격'] = pd.to_numeric( self.df['가격'] , errors='coerce' ).fillna(0)
#         self.df['연도'] = self.df['연도'] = self.df['출판년월'].str.slice(0,4)

#     def __getstate__(self):   
#         average_p = self.df['가격'].mean()
#         highest_p = self.df['가격'].max()
#         lowest_p = self.df['가격'].min()
#         mostpublish = self.df['연도'].value_counts()
#         return {   "평균가격": int(average_p) ,
#             "최고가격": int(highest_p) ,
#             "최저가격": int(lowest_p) ,
#             "최다출판연도": int(mostpublish)  }
# Book_Service = BookService()