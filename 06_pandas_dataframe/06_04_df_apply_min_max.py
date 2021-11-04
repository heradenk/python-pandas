# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:07:00 2021

@author: YOO
"""

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('\n')

# 사용자 함수 정의
def min_max(x):                   # 최대값 - 최소값
    return x.max() - x.min()

# 데이터프레임에 apply 메소드 적용
result = df.apply(min_max)        # 기본값 axis=0
print(result)
print('\n')
print(type(result))