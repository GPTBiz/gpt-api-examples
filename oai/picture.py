from openai import OpenAI

BASE_URL = "https://endpoints.gpt.biz/v1"
APi_KEY = "YOUR API_KEY"

client = OpenAI(base_url=BASE_URL, api_key=APi_KEY)

prompt = "An astronaut lounging in a tropical resort in space, pixel art"
model = "dall-e-3"


response = client.images.generate(prompt=prompt, model=model)

# Prints response containing a URL link to image
print(response)

