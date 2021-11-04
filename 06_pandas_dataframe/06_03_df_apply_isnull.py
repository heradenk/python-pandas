# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:02:46 2021

@author: YOO
"""

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')

# 사용자 함수 정의
def missing_value(series):      # 시리즈를 인자로 전달
    return series.isnull()      # 불린 시리즈를 반환

# 데이터프레임에 apply 메소드를 적용
result = df.apply(missing_value, axis=0)
print(result.head())
print('\n')
print(type(result))
