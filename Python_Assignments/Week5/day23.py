import json

data = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}

with open('data.json', 'w', encoding='utf-8') as f:
    # json.dump() 함수는 기본적으로 모든 입력을 유니코드 이스케이프 시퀀스로 변환
    ## ensure_ascii=True (DEFAULT)
    ## ensure_ascii=False로 지정해주면 한글이 변환되지 않고 그대로 저장
    json.dump(data, f, ensure_ascii=False, indent=4)

import requests

url = "https://randomuser.me/api/"

r = requests.get(url)

data = json.loads(r.text)
# data format:
"""{
    "results": [...],
    "info": ""
}"""
# results format:
"""[{
    "gender": "",
    "name": "",
    ...
}]"""
name = data["results"][0]["name"]

# name format:
"""{
    "title": "",
    "first": "",
    "last": ""
}"""
print(f"First name: {name["first"]}, Last name: {name["last"]}")