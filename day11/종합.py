import numpy as np

data = np.genfromtxt(
    "./day11/team/layoffs_events.csv",
    delimiter=",",
    filling_values=0,
    invalid_raise=False,
    skip_header=1,
    encoding="utf-8",
    dtype=str,
)
print(f"데이터 형태: {data.shape}")
print(data)


# 1. 해고 인원수 (데이터 기초 현황 진단)
fire = data[:,2]
x = np.where( x  == '' , '0'  ,  x )
print( x[ : 100 ].astype(int))

company = data["company"]
print(company)



# 총 해고수 , 최대인원 해고한 기업 , 최소인원 해고한 기
print(np.sum(fire))
max1 = np.argmax(fire)
min1 = np.argmin(fire)
print(data[min1])
print(data[max1])

fire_average = np.mean(fire)
print(fire_average)

industry = data["industry"]

unique_industry = np.unique(industry)

for ind in unique_industry:
    total = np.sum(fire[industry == ind])
    print(ind, total)

ai = data['ai_bool']
print(ai)

target1 = (fire >= fire_average) & (ai == True)
target2 = (fire >= fire_average) & (ai == False)
print(company[target1])
print(company[target2])

fire_1 = np.percentile(fire , 90)
print(fire_1)
con1 = (fire>=fire_1) & (ai==True)
con2 = (fire>=fire_1) & (ai==False)
con3 = fire>=fire_1
print(company[con1])
print(company[con2])
print(company[con3])
z = (industry[con3])
x = (industry[con1])

print(x)

inds , counts = np.unique(z , return_counts=True)
print(inds , counts)
count = counts.astype(int)
indss = inds

qqq = np.vstack((indss , count))
print(qqq)


# 해고인원이 상위 10%인 기업이 속한 산업군 + 산업군 내 AI기업 수
top10 = fire >= np.percentile(fire,90)

for ind in np.unique(industry[top10]):
    total = np.sum((top10) &(industry==ind))
    ai_n = np.sum((top10) &(industry==ind) &(ai==True))
    print(ind, total, ai_n)


ai_company = company[ai]
ai_true = ai==True
ai_false =ai ==False


print(np.sum(ai_true))
print(np.sum(ai_false))

# ai 트루인 회사수
print(np.sum(fire[ai_true]))
print(np.sum(fire[ai_false]))

# 해고 위험 산업군
