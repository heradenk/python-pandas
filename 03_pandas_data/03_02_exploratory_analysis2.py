# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:53:51 2021

@author: YOO
"""

import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'culinders', 'displacement', 'horsepower', 'weight',
             'acceleration', 'model year', 'origin', 'name']

# 데이터 프레임 df의 각 열이 가지고 있는 원소 개수 확인
print(df.count())
print('\n')

# df.count()가 반환하는 객체 타입 출력
print(type(df.count()))

# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인
unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')

# value_counts 메소드가 변환하는 객체 타입 출력
print(type(unique_values))
