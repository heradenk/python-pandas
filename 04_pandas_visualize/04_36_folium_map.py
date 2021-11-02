# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:16:12 2021

@author: YOO
"""

# 라이브러리 불러오기
import folium

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], zoom_start=12)

# 지도를 HTML파일로 저장하기
seoul_map.save('./seoul.html')