## 使用

### imagine

文生图

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "imagine",
    "data": {
      "prompt": "a cute cat"
    }
}'
```

图生图，需带上图片 URL

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "imagine",
      "data": {
        "prompt": "a cute cat",
        "picurl": "https://xxxxxx/xxxxxxxxxxxx.jpg"
      }
}'
```

### upscale

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "upscale",
    "data": {
      "index": 1,
      "msg_id": "xxxxxxxxxx",
      "msg_hash": "xxxxx-xxx-xxxx-xxxx-xxxxxx",
      "trigger_id": "xxxxxxxxxx"
    }
}'
```

- `index`: 图片索引，取值：1、2、3、4
- `msg_id`: `imagine` 绘画完成后回调报文 `id` 字段
- `msg_hash`: `imagine` 绘画完成后回调报文 `attachments[0].filename.split("_")[-1].split(".").[0]`
- `trigger_id`: `imagine` 绘画完成后回调报文 `trigger_id` 字段

### variation

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "variation",
    "data": {
      "index": 1,
      "msg_id": "xxxxxxxxxx",
      "msg_hash": "xxxxx-xxx-xxxx-xxxx-xxxxxx",
      "trigger_id": "xxxxxxxxxx"
    }
}'
```

### solo_variation

对 `upscale` 的单张图片进行 "Make Variations" 操作

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "solo_variation",
    "data": {
      "index": 1,
      "msg_id": "xxxxxxxxxx",
      "msg_hash": "xxxxx-xxx-xxxx-xxxx-xxxxxx",
      "trigger_id": "xxxxxxxxxx"
    }
}'
```

- `index`: 图片索引，此处无用，取值：1
- `msg_id`: `upscale` 绘画完成后回调报文 `id` 字段
- `msg_hash`: `upscale` 绘画完成后回调报文 `attachments[0].filename.split("_")[-1].split(".").[0]`
- `trigger_id`: `upscale` 绘画完成后回调报文 `trigger_id` 字段

### solo_low_variation

对 `upscale` 的单张图片进行 "Vary(Subtle)" 操作

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "solo_low_variation",
    "data": {
      "index": 1,
      "msg_id": "xxxxxxxxxx",
      "msg_hash": "xxxxx-xxx-xxxx-xxxx-xxxxxx",
      "trigger_id": "xxxxxxxxxx"
    }
}'
```

- `index`: 图片索引，此处无用，取值：1
- `msg_id`: `upscale` 绘画完成后回调报文 `id` 字段
- `msg_hash`: `upscale` 绘画完成后回调报文 `attachments[0].filename.split("_")[-1].split(".").[0]`
- `trigger_id`: `upscale` 绘画完成后回调报文 `trigger_id` 字段

### solo_high_variation

对 `upscale` 的单张图片进行 "Vary(Strong)" 操作

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "solo_high_variation",
    "data": {
      "index": 1,
      "msg_id": "xxxxxxxxxx",
      "msg_hash": "xxxxx-xxx-xxxx-xxxx-xxxxxx",
      "trigger_id": "xxxxxxxxxx"
    }
}'
```

- `index`: 图片索引，此处无用，取值：1
- `msg_id`: `upscale` 绘画完成后回调报文 `id` 字段
- `msg_hash`: `upscale` 绘画完成后回调报文 `attachments[0].filename.split("_")[-1].split(".").[0]`
- `trigger_id`: `upscale` 绘画完成后回调报文 `trigger_id` 字段


### zoomout

对 `upscale` 的单张图片进行 Zoom Out 2x/1.5x 操作

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "solo_high_variation",
    "data": {
      "msg_id": "xxxxxxxxxx",
      "msg_hash": "xxxxx-xxx-xxxx-xxxx-xxxxxx",
      "zoomout": 50
      "trigger_id": "xxxxxxxxxx"
    }
}'
```

- `zoomout`: 图片扩大（Outpaint）系数，2x -> 50、1.5x -> 75


### expand

对 `upscale` 的单张图片进行某方向的扩展操作

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "expand",
    "data": {
      "msg_id": "xxxxxxxxxx",
      "msg_hash": "xxxxx-xxx-xxxx-xxxx-xxxxxx",
      "direction": "up"
      "trigger_id": "xxxxxxxxxx"
    }
}'
```

- `direction`: 图片扩大方向，取值：left/right/up/down


### reset

```bash
curl -X 'POST' \
  'https://endpoints.gpt.biz/v1/images/midjourney' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR API_KEY' \
  -d '{
    "type": "reset",
    "data": {
      "msg_id": "xxxxxxxxxx",
      "msg_hash": "xxxxx-xxx-xxxx-xxxx-xxxxxx",
      "trigger_id": "xxxxxxxxxx"
    }
}'
```