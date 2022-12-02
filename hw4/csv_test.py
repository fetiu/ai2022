from csv import DictReader



with open('metro-toilets.csv', 'r', encoding='cp949') as f:
    data = DictReader(f);
    for row in data:
        print(f'{row["화장실명"]} {row["위도"]} {row["경도"]}')

with open('gyeonggi-toilets.csv', 'r', encoding='cp949') as f:
    data = DictReader(f);
    for row in data:
        print(f'{row["화장실명"]} {row["위도"]} {row["경도"]}')

with open('seoul-toilets2.csv', 'r') as f:
    data = DictReader(f);
    for row in data:
        print(f'{row["화장실명"]} {row["위도"]} {row["경도"]}')