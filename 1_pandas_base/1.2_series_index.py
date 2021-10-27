# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 01:17:38 2021

@author: YOO
"""

import pandas as pd

# 리스트를 시리즈를 변환하여 변수 sr에 저장
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# 인덱스 배열은 변수 idx에 저장, 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print(idx)
print('\n')
print(ValueError)