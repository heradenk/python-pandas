# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:32:11 2021

@author: YOO
"""

# 라이브러리 불러오기
import matplotlib

# 컬러 정보를 담은 빈 딕셔너리 생성
colors={}

# 컬러 이름과 헥사코드 확인하여 딕셔너리에 입력
for name, hex in matplotlib.colors.cnames.items():
    colors[name] = hex
    
# 딕셔너리 출력
print(colors)