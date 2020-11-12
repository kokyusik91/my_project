from pymongo import MongoClient
import requests
import json


client = MongoClient('localhost', 27017)
db = client.sparta

url_items = 'http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/basedList?ServiceKey=Di38GMRBGgQb5g5dSuC0bFOuiyBVsohJ2OiwbPbg5Vx9Er94by5lIAeT4TzrcG61x5qoU0tGFeW86DC5KJ7trQ%3D%3D&MobileOS=ETC&numOfRows=100&pageNo=1&MobileApp=TestApp&_type=json'
response = requests.get(url_items)


dict = json.loads(response.text)
print(dict['response']['body']['totalCount'])
camp_info =dict['response']['body']['items']['item']
# print(camp_info)

for camp_item in camp_info:
   print(camp_item['facltNm'], camp_item['addr1'])
   # print('주소 :' ,camp_item['addr1'],' / 이름 :', camp_item['facltNm'])
   # address = camp_item['addr1']
   # camp_name = camp_item['facltNm']
   #
   #
   # doc = {
   #    'address': address,
   #    'camp_name' : camp_name
   # }
   #  print(doc)
   # db.camping.insert_one(doc)