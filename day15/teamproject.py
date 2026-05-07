import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import seaborn as sns

# [판다스 불러오기]
df = pd.read_csv("./day15/train_HousePrices.csv")
df.info()
print(df.isnull().sum())

# 1. 데이터 전처리
# 1-1. 수치형 변수 결측치 처리: 'LotFrontage', 'MasVnrArea', 'GarageYrBlt' 등의 수치형 변수의 결측치는 데이터의 중앙값(Median)으로 대체하여 보정한다.
df['GrLivArea'] = df['GrLivArea'].fillna( df['GrLivArea'].median() )
df['SalePrice'] = df['SalePrice'].fillna( df['SalePrice'].median() )
print( df.isnull().sum() )

# 1-2. 범주형 변수 결측치 처리 (정보 부재 명확): 정보 부재가 명확한 범주형 변수('Alley', 'PoolQC', 'Fence' 등)는 결측치를 'NoAlley', 'NoPool', 'NoFence'와 같이 특정 문자열로 대체한다
df['RoofStyle'] = df['RoofStyle'].fillna( 'NoRoofStyle' )
df['HouseStyle'] = df['HouseStyle'].fillna( 'NoHouseStyle' )
print( df.isnull().sum() )

# 1-3. 범주형 변수 결측치 처리 (일반)
df['Exterior1st'] = df['Exterior1st'].fillna( df['Exterior1st'].mode()[0] )
print( df.isnull().sum() )


# 2. 데이터 시각화 및 분석
# 2-1. 주택 판매 가격(SalePrice) 분포 분석
# 2-2. 주거 면적과 가격 관계 분석 (가설 1 검증)

# 2-3. 주택 스타일별 가격 분포 비교 (가설 2 검증) ***********************
# sns.boxplot을 사용하여 주택 스타일(HouseStyle)별 가격 분포와 이상치(Outlier)를 파악한다.
print(df['HouseStyle'].head())
sns.boxplot( x = 'HouseStyle', y = 'SalePrice' , data = df )
plt.title('주택 스타일별 가격 분포 비교')
plt.xlabel('주택 스타일(HouseStyle)')
plt.ylabel('가격(SalePrice)')
plt.show()


# 2-4. 주요 외관 요소별 가격 분포 비교 (가설 2 검증)
# 2-5. 상관관계 시각화 및 핵심 인자 도출 (가설 3 검증)