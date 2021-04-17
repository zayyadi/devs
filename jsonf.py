import requests
import json
res = requests.get('http://httpbin.org/get')
#print(res.status_code)  
#print(res.text)    
resj = res.json()

json_str = json.dumps(resj)
resp = json.loads(json_str)
#print (resp)
for values in resp:
    print (resp[values])