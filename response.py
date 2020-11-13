
# 응답 코드

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.sparta

@app.route('/')
def home():
   return render_template('camping_search.html')

@app.route('/list', methods=['POST'])
def camping_info():
   sido_receive = request.form['sido_give']

   if sido_receive == '서울':
      regex = '^' + sido_receive
   elif sido_receive == '충청':
      regex = '^충청|충남|충북'
   elif sido_receive == '경상':
      regex = '^경상|경남|경북'
   elif sido_receive == '전라':
      regex = '^전라|전남|전북'
   elif sido_receive == '경기':
      regex = '^' + sido_receive
   elif sido_receive == '강원':
      regex = '^' + sido_receive
   elif sido_receive == '제주':
      regex = '^' + sido_receive

   # print(sido_receive)
   real_address = list(db.camping_data.find({'address': { '$regex': regex, '$options': 'i' }},{'_id': 0}))
   # print(real_address)

   return jsonify({'result': 'success', 'list': real_address})
   # # return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

