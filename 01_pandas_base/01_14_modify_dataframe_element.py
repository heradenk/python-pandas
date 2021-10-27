# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:38:25 2021

@author: YOO
"""

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)

# 데이터 프레임 df의 원소 여러 개를 변경하는 방법: '서준'의 '음악', '체육' 점수
df.loc[ 0, ['음악', '체육']] = 50
print(df)
print('\n')

df.loc[ 0, ['음악', '체육']] = 100, 50
print(df)