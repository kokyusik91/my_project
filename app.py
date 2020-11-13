
# db에 데이터 저장하는 코드

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests
import json

# app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.sparta

# @app.route('/')
# def home():
#    return render_template('camping_search.html')

url_items = 'http://api.visitkorea.or.kr/openapi/service/rest/GoCamping/basedList?ServiceKey=Di38GMRBGgQb5g5dSuC0bFOuiyBVsohJ2OiwbPbg5Vx9Er94by5lIAeT4TzrcG61x5qoU0tGFeW86DC5KJ7trQ%3D%3D&MobileOS=ETC&numOfRows=2526&pageNo=1&MobileApp=TestApp&_type=json'
response = requests.get(url_items)
#
#
dict = json.loads(response.text)
# # print(dict['response']['body']['totalCount'])
camp_info =dict['response']['body']['items']['item']
# # print(camp_info)

for camp_item in camp_info:
   # print(camp_item['facltNm'], camp_item['addr1'], camp_item['mapX'], camp_item['mapY'])
   # print('주소 :' ,camp_item['addr1'],' / 이름 :', camp_item['facltNm'])
   address = camp_item['addr1']
   camp_name = camp_item['facltNm']
   mapX = camp_item['mapX']
   mapY = camp_item['mapY']
   contentId = camp_item['contentId']

   # doc = {
   #
   #    'address': address,
   #    'camp_name': camp_name,
   #    'mapX': mapX,
   #    'mapY': mapY,
   #    'camp_id': contentId
   # }
   #
   # db.camping_data.insert_one(doc)
   print(address)
# real_address = list(db.camping_data.find({'address': {'$regex' "경기"}}))
# for real_add in real_address:
#    print(real_add)

# @app.route('/list', methods=['POST'])
# def camping_info():
#    sido_receive = request.form['sido']
#    real_address = list(db.camping_data.find({'address':}))
#    print(real_address)
#    return jsonify({'list': real_address})
#
#
#
# app.run('0.0.0.0', port=5000, debug=True)

