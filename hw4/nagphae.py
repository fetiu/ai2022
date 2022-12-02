#!/usr/local/bin/python
import json, requests
from sys import argv
from geopy.geocoders import Nominatim

def locate_approx():
    loc = {}
    req = requests.get("http://www.geoplugin.net/json.gp")
    if req.status_code == 200:
        payload = json.loads(req.text)
        loc['lat'] = float(payload['geoplugin_latitude'])
        loc['lon'] = float(payload['geoplugin_longitude'])
    return loc

def loc2addr(lat, lon):
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = geolocoder.reverse(f'{lat}, {lon}')
    words = str(address).split(',');
    return ''.join(reversed(words))

msg = argv[1];

try:
    loc = json.loads(argv[2]);
except:
    loc = locate_approx();

def calc_dist(dx, dy):
    return (dx**2 + dy**2)**(1/2)

nearest = {'lat': 0, 'lon': 0, 'name': None, 'dist': float('inf')};

def update_nearest(toilets):
    for t in toilets:
        dx, dy = (0,0)
        try:
            dx = float(t['위도']) - float(loc['lat']);
            dy = float((t['경도'])) - float(loc['lon'])
        except:
            continue

        dist = calc_dist(dx, dy)
        if (nearest['dist'] > dist):
            nearest['lat'] = t['위도']
            nearest['lon'] = t['경도']
            nearest['name'] = t['화장실명']
            nearest['dist'] = dist

def get_nearest_toilet():
    from csv import DictReader

    with open('metro-toilets.csv', 'r', encoding='cp949') as f:
        data = DictReader(f);
        update_nearest(data);

    with open('gyeonggi-toilets.csv', 'r', encoding='cp949') as f:
        data = DictReader(f);
        update_nearest(data);

    with open('seoul-toilets2.csv', 'r') as f:
        data = DictReader(f);
        update_nearest(data);

    return nearest

nearwords = ['근처', '근방', '가까운']
quitwords =  ['없어', '괜찮아', '종료', '그만', '끝']
mapwords = ['지도', '길', '위치', '약도', '그림', '맵', '주소']
for word in msg.split():
    if word in quitwords:
        print('끝')
    if word in nearwords:
        print(f"{nearest['name']}에 가장 가까운 화장실이 있어요. ")
    if word in mapwords:
        print(loc2addr(nearest['lat'], nearest['lon']))

# TODO: print location data as coordinate