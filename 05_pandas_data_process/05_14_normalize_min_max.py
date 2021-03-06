# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:10:08 2021

@author: YOO
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:59:58 2021

@author: YOO
"""

# 라이브러리 불러오기
import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# horsepower 열의 누락 데이터('?')를 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)     # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)  # 누락 데이터 행 삭제
df['horsepower'] = df['horsepower'].astype('float')     # 문자열을 실수형으로 변환

# horsepower 열의 통계 요약 정보로 최대값(max)과 최소값(min) 확인
print(df.horsepower.describe())
print('\n')

# horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
min_x = df.horsepower - df.horsepower.min()
min_max = df.horsepower.max() - df.horsepower.min()
df.horsepower = min_x/min_max

print(df.horsepower.head())
print('\n')
print(df.horsepower.describe())