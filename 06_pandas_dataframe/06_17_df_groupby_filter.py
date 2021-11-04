# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:40:50 2021

@author: YOO
"""

# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 분할
grouped = df.groupby(['class'])

# 각 그룹에 대한 모든 열의 표준 편차를 집계하여 데이터프레임으로 반환
std_all = grouped.std()
print(std_all)
print('\n')
print(type(std_all))
print('\n')

# 각 그룹에 대한 fare 열의 표준편차를 집계하여 시리즈로 반환
std_fare = grouped.fare.std()
print(std_fare)
print('\n')
print(type(std_fare))

# 그룹 객체에 agg() 메소드 적용 - 사용자 정의 함수를 인자로 전달
def min_max(x):     # 최대값 - 최소값
    return x.max() - x.min()

# 각 그룹의 ㅣ최대값과 최소값의 차이를 계산하여 그룹별로 집계
agg_minmax = grouped.agg(min_max)
print(agg_minmax.head())

# 여러 함수를 각 열에 동일하게 적용하여 집계
agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())
print('\n')

# 각 열마다 다른 함수를 적용하여 집계
agg_sep = grouped.agg({'fare':['min', 'max'], 'age':'mean'})
print(agg_sep.head())

# 그룹별 age 열의 평균 집계 연산
age_mean = grouped.age.mean()
print(age_mean)
print('\n')

# 그룹별 age 열의 표준편차 집계 연산
age_std = grouped.age.std()
print(age_std)
print('\n')

# 그룹 객체의 age 열을 iteration으로 z-score를 계산하여 출력
for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key])/age_std.loc[key]
    print('* origin :', key)
    print(group_zscore.head(3))     # 각 그룹의 첫 3개의 행 출력
    print('\n')
    
# z-score를 계산하는 사용자 함수 정의
def z_score(x):
    return (x - x.mean())/x.std()

# transform() 메소드를 이용하여 age 열의 데이터를 z-score로 변환
age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]])        # 1, 2, 3 그룹의 첫 데이터 확인(변환 결과)
print('\n')
print(len(age_zscore))                  # transform 메소드 반환 값의 길이
print('\n')
print(age_zscore.loc[0:9])              # transform 메소드 반환 값 출력(첫 10개)
print('\n')
print(type(age_zscore))                 # transform 메소드 반환 객체의 자료형

# 데이터 개수가 200개 이상인 그룹만을 필터링하여 데이터프레임으로 반환
grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter.head())
print('\n')
print(type(grouped_filter))

# age 열의 평균이 30보다 작은 그룹만을 필터링하여 데이터프레임으로 반환
age_filter = grouped.filter(lambda x: x.age.mean() < 30)
print(age_filter.tail())
print('\n')
print(type(age_filter))