import requests
import json
res = requests.get('http://httpbin.org/get')
print(res.status_code)  
print(res.text)    

for i in res.json():
    print (i)