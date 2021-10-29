# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:39:04 2021

@author: YOO
"""

import pandas as pd

# read_scv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 데이터프레임 df의 내용을 일부 확인
print(df.head())    # 처음 5개 행
print('\n')
print(df.tail())    # 마지막 5개 행

# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 튜플로 반환
print(df.shape)
print('\n')

# 데이터프레임 df의 내용 확인
print(df.info())
print('\n')

# 데이터프레임 df의 자료형 확인
print(df.dtypes)
print('\n')

# 시리즈 (mog 열)의 자료형 확인
print(df.mpg.dtypes)

# 데이터프레임 df의 기술 통계 정보 확인
print(df.describe())
print('\n')
print(df.describe(include='all'))
