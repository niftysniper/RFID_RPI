import requests
import random
import datetime

ts = datetime.datetime.utcnow();
UID = random.randint(0,99999999999)
payLoad = {
  'UID': UID,
  'timeStamp' : ts
}
r = requests.get('https://httpbin.org/post', params = payLoad)

print(r.url)
