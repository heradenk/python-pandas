# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:52:05 2021

@author: YOO
"""

## google 지오코딩 API를 통해 위도, 경도 데이터 가죠오기

# 라이브러리 가져오기

import googlemaps
import pandas as pd

my_key = "---key-----"

# 구글맵스 객체 생성하기
maps = googlemaps.Client(key=my_key) # my key값 입력

lat = [] # 위도
lng = [] # 경도

# 장소(또는 주소) 리스트
places = ["서울시청", "국립국악원", "해운대해수욕장"]

i=0
for place in places:
    i = i + 1
    try:
        print(i, place)
        # 지오코딩 API 결과값 호출하여 geo_location 변수에 저장
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
        
    except:
        lat.append('')
        lng.append('')
        print(i)
        
# 데이터프레임으로 변환하기
df = pd.DataFrame({'위도':lat, '경도':lng}, index=places)
print('\n')
print(df)