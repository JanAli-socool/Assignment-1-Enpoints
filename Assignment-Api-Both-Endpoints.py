#First Api-EndPoint by using "GET" Method.

import requests,json

url = "https://api.math.tools/numbers/pi"

payload = ""
headers = {
  'X-MathTools-Api-Secret': '',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


json_string = response.text
json_string[0]
data = json.loads(json_string)

data = response.json()

print(data)

#Second Api-EndPoint by using "GET" Method.
import requests,json

url = "https://api.math.tools/numbers/nod"

payload = ""
headers = {
  'Api Key' : 'X-MathTools-Api-Secret'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


json_string = response.text
json_string[0]
data = json.loads(json_string)

data = response.json()

print(data)