# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:20:58 2021

@author: YOO
"""

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]

# 각 열의 NaN 찾기 - 데이터프레임을 전달하면 데이터프레임 반환
def missing_value(x):
    return x.isnull()

# 각 열의 NaN 개수 반환 - 데이터프레임을 전달하면 시리즈 반환
def missing_count(x):
    return missing_value(x).sum()

# 데이터프레임의 총 NaN 개수 - 데이터프레임을 전달하면 값 반환
def total_number_missing(x):
    return missing_count(x).sum()

# 데이터프레임에 함수 매핑
result_df = df.pipe(missing_value)
print(result_df.head())
print(type(result_df))

result_series = df.pipe(missing_count)
print(result_series)
print(type(result_series))

result_value = df.pipe(total_number_missing)
print(result_value)
print(type(result_value))