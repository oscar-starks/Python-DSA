import requests
import json

url = "https://tentendata.com.ng/api/data/"

payload = "{\"network\": 4,\r\n\"mobile_number\": \"09017741269\",\r\n\"plan\": 224,\r\n\"Ported_number\":true}"
headers = {
  'Authorization': 'Token your_authorization_token',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)