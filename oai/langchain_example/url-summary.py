import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

BASE_URL = "https://endpoints.gpt.biz/v1"
APi_KEY = "YOUR API_KEY"

os.environ["OPENAI_API_KEY"] = APi_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL

# 
url="https://xxxx"

if "youtube.com" in url:
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
else:
    loader = UnstructuredURLLoader(urls=[url], ssl_verify=False, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
data = loader.load()

llm = ChatOpenAI(temperature=0, model="gpt-4o")
prompt_template = """Write a summary of the following in 250-300 words:
                    
{text}

"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
summary = chain.run(data)
print(summary)