import requests
import json

APi_KEY = "YOUR API_KEY"
BASE_URL = "https://endpoints.gpt.biz/v1/images/midjourney"

# text to image
payload = json.dumps({
  "type": "imagine",
  "data": {
    "prompt": "man angry face looking down, low angle, illustration style"
  }
})
headers = {
  'Authorization': f'Bearer {APi_KEY}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", BASE_URL, headers=headers, data=payload)

print(response.text)

#query Task
trigger_id = "XXXX"
headers = {
  'Authorization': f'Bearer {APi_KEY}',
}

response = requests.request("GET", BASE_URL + trigger_id, headers=headers, data={}) 