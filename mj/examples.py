import requests
import json

API_KEY = "YOUR_API_KEY"

headers = {
  'Authorization': 'Bearer GB-Sm0YFesibqs8a2iN-hsJjWecunCcnajEf2kahmW2e2lXFFPiugTQ9U_MhQRleZku',
  'Content-Type': 'application/json'
}

"""
- trigger_id: 触发任务后响应报文中的 trigger_id字段
- msgId: 图片绘制后回调报文中的id字段 
- hash: 图片绘制后回调报文中的hash字段

**图片绘制进度可通过"查询任务进度"接口查看**
"""

# 查询任务进度
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney/<trigger_id>", headers=headers, data="")
print(resp.text)


# 文生图
payload = json.dumps({
  "type": "imagine",
  "data": {
    "prompt": "a cute cat",
    "mode": "relax",
    "picUrl": []
  }
})
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney", headers=headers, data="")
print(resp.text)


# describe  - 图片生成prompt
payload = json.dumps({
  "type": "describe",
  "data": {
    "imgUrl": "https://xxxxxxxxxxxx",
  }
})
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney", headers=headers, data="")
print(resp.text)


# variation
payload = json.dumps({
  "type": "variation",
  "data": {
    "index": 1,
    "msgId": "xxxxxxxxxxxxxx",
    "hash": "xxxxxxxxxxxxxxx",
    "trigger_id": "xxxxxxxxxxxxxxxx",
    "prompt": "xxxxxx"  #选填
  }
})
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney", headers=headers, data="")
print(resp.text)


# upscale
payload = json.dumps({
  "type": "upscale",
  "data": {
    "index": 1,
    "msgId": "xxxxxxxxxxxxxx",
    "hash": "xxxxxxxxxxxxxxx",
    "trigger_id": "xxxxxxxxxxxxxxxx"
  }
})
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney", headers=headers, data="")
print(resp.text)


# zoomout - 对 `upscale` 的单张图片进行 Zoom Out 2x/1.5x 操作
payload = json.dumps({
  "type": "zoomout",
  "data": {
    "zoomout": 50, # 图片扩大（Outpaint）系数，2x -> 50、1.5x -> 75
    "msgId": "xxxxxxxxxxxxxx",
    "hash": "xxxxxxxxxxxxxxx",
    "trigger_id": "xxxxxxxxxxxxxxxx"
  }
})
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney", headers=headers, data="")
print(resp.text)


# expand  - 对 `upscale` 的单张图片进行某方向的扩展操作
payload = json.dumps({
  "type": "expand",
  "data": {
    "direction": "up", # 图片扩大方向，取值：left/right/up/down
    "msgId": "xxxxxxxxxxxxxx",
    "hash": "xxxxxxxxxxxxxxx",
    "trigger_id": "xxxxxxxxxxxxxxxx"
  }
})
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney", headers=headers, data="")
print(resp.text)


# reset   - 重绘
payload = json.dumps({
  "type": "reset",
  "data": {
    "msgId": "xxxxxxxxxxxxxx",
    "hash": "xxxxxxxxxxxxxxx",
    "trigger_id": "xxxxxxxxxxxxxxxx"
  }
})
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney", headers=headers, data="")
print(resp.text)


# solo_low_variation  - 对 `upscale` 的单张图片进行 "Vary(Subtle)" 操作
payload = json.dumps({
  "type": "solo_low_variation",
  "data": {
    "msgId": "xxxxxxxxxxxxxx",
    "hash": "xxxxxxxxxxxxxxx",
    "trigger_id": "xxxxxxxxxxxxxxxx"
  }
})
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney", headers=headers, data="")
print(resp.text)


# solo_low_variation  - 对 `upscale` 的单张图片进行 "Vary(Strong)" 操作
payload = json.dumps({
  "type": "solo_high_variation",
  "data": {
    "msgId": "xxxxxxxxxxxxxx",
    "hash": "xxxxxxxxxxxxxxx",
    "trigger_id": "xxxxxxxxxxxxxxxx"
  }
})
resp = requests.get("https://endpoints.cn.gpt.biz/v1/images/midjourney", headers=headers, data="")
print(resp.text)

