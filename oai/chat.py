from openai import OpenAI

BASE_URL = "https://endpoints.gpt.biz/v1"
APi_KEY = "YOUR API_KEY"

client = OpenAI(base_url=BASE_URL, api_key=APi_KEY)

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)


# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content, end="")