# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:05:27 2021

@author: YOO
"""

import pandas as pd

# 판다스 DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
data = {'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True) # name 열을 인덱스로 지정
print(df)

# to_json() 메소드를 사용하여 JSON 파일로 내보내기. 파일명은 df_sample.json으로 저장
df.to_json("./df_sample.json")