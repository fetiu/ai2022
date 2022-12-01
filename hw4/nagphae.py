#!/usr/local/bin/python
import json
from sys import argv
from geopy.geocoders import Nominatim

def geocoding_reverse(lat_lng_str):
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = geolocoder.reverse(lat_lng_str)
    return address

try:
    loc = json.loads(argv[1]);
except:
    raise Exception("Error loading json");

print(loc['msg'])
quitwords =  ['없어', '괜찮아', '종료', '그만', '끝']
for word in loc['msg'].split():
    print(word)
    if word in quitwords:
        print("끝")
        quit(); 

print("가장 가까운 화장실 정보에요. ")
address = geocoding_reverse(f"{loc['lat']}, {loc['lon']}")
print(address)
