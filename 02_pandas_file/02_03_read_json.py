# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:30:53 2021

@author: YOO
"""

import pandas as pd

# read_json() 함수로 데이터프레임 변환
df = pd.read_json('./read_json_sample.json')
print(df)
print('\n')
print(df.index)
