# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:12:54 2021

@author: YOO
"""

import pandas as pd

# read_excel() 함수로 데이터프레임 변환
df1 = pd.read_excel('./남북한발전전력량.xlsx', engine= 'openpyxl')  # header=0 (default옵션)
df2 = pd.read_excel('./남북한발전전력량.xlsx', engine= 'openpyxl', header=None) # header 옵션 미적용

# 데이터프레임 출력
print(df1)
print('\n')
print(df2)