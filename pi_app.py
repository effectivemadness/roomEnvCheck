import datetime
import Adafruit_DHT as dht
import requests, json

URL = 'http://192.168.0.13:8888/update'
#온습도센서 모듈에 따라 DHT11, DHT22 변경해야 함
#DHT센서의 핀번호 보통 4를 입력

h,t = dht.read_retry(dht.DHT11,4)
print (h, t)
data = {'temp': t, 'humid': h}
headers = {'Content-Type': 'application/json; charset=utf-8'}
res = requests.post(URL,headers=headers, data=json.dumps(data))
print(res)