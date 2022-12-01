#!/usr/local/bin/python
import json
from sys import argv
from geopy.geocoders import Nominatim

def loc2addr(lat, lon):
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = geolocoder.reverse(f'{lat}, {lon}')
    words = str(address).split(',');
    return ''.join(reversed(words))

try:
    loc = json.loads(argv[1]);
except:
    raise Exception('Error loading json');

def calc_dist(dx, dy):
    return (dx**2 + dy**2)**(1/2)

from csv import DictReader

nearest = {'lat': 0, 'lon': 0, 'name': None, 'dist': float('inf')};

def update_nearest(toilets):
    for t in toilets:
        dx, dy = (0,0)
        try:
            dx = float(t['위도']) - float(loc['lat']);
            dy = float((t['경도'])) - float(loc['lon'])
        except:
            continue
            # print(f'{t['화장실명']} {t['위도']} {t['경도']}')
        dist = calc_dist(dx, dy)
        if (nearest['dist'] > dist):
            nearest['lat'] = t['위도']
            nearest['lon'] = t['경도']
            nearest['name'] = t['화장실명']
            nearest['dist'] = dist
        # print(f'{t['화장실명']} {t['위도']} {t['경도']}')

with open('metro-toilets.csv', 'r', encoding='cp949') as f:
    data = DictReader(f);
    update_nearest(data);

with open('gyeonggi-toilets.csv', 'r', encoding='cp949') as f:
    data = DictReader(f);
    update_nearest(data);

with open('seoul-toilets2.csv', 'r') as f:
    data = DictReader(f);
    update_nearest(data);

quitwords =  ['없어', '괜찮아', '종료', '그만', '끝']
mapwords = ['지도', '길', '위치', '약도', '그림', '맵']
for word in loc['msg'].split():
    if word in quitwords:
        print('끝')
        quit();
    if word in mapwords:
        quit();

if nearest['name'] is None:
    print(f'가까운 화장실을 찾지 못했어요 ');
else:
    print(f"{nearest['name']}이 가장 가까운 화장실이에요. 주소는")
    print(loc2addr(nearest['lat'], nearest['lon']), '에요.')
