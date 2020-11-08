import requests
import json

url_items = "http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/locationBasedList?serviceKey=Di38GMRBGgQb5g5dSuC0bFOuiyBVsohJ2OiwbPbg5Vx9Er94by5lIAeT4TzrcG61x5qoU0tGFeW86DC5KJ7trQ%3D%3D&pageNo=1&numOfRows=100&MobileOS=ETC&MobileApp=AppTest&mapX=128.6142847&mapY=36.0345423&radius=2000&_type=json"
response = requests.get(url_items)
dict = json.loads(response.text)

camp_info =dict['response']['body']['items']['item']


for camp_item in camp_info:
   print(camp_item['intro'])
