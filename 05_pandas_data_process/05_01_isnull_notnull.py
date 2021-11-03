# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:24:56 2021

@author: YOO
"""

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# deck 열의 NAN 개수 계산하기
nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)

# isnull() 메소드로 누락 데이터 찾기
print(df.head().isnull())

# notnull() 메소드로 누락 데이터 찾기
print(df.head().notnull())

# isnull() 메소드로 누락 데이터 개수 구하기
print(df.head().isnull().sum(axis=0))