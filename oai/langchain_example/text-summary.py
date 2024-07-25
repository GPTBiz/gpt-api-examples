from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
from langchain_community.docstore.document import Document
from langchain_text_splitters import CharacterTextSplitter
import os

BASE_URL = "https://endpoints.gpt.biz/v1"
APi_KEY = "YOUR API_KEY"

os.environ["OPENAI_API_KEY"] = APi_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL

source_text="""
OpenAI 最近发布的 GPT-4o mini 模型引发了广泛关注，从规模和性能上展现了一些显著特点。

首先，从模型规模来看，GPT-4o mini 相比其前身 GPT-4 的 1.8 万亿参数大幅缩小，目前规模约为 10 亿参数。尽管 OpenAI 尚未公开确切参数，但有消息指出该模型的规模介于 1-10 亿之间，与 Meta 的 LLaMA 8B 属于同一层级​ (AOL.com)​​ (InfoDocket)​。

GPT-4o mini 的核心驱动力是高质量的数据，而这些数据主要来源于更大模型生成的“合成数据”。Andrej Karpathy 强调，这种合成数据具有干净可控、结构清晰和目的明确的特点，特别是在数学和代码领域受益显著。这种数据质量的提升，使得小模型在处理特定任务时能够表现得更加出色​ (InfoDocket)​。

小模型对垃圾数据的噪音更加敏感，因此数据的质量比数量更重要。OpenAI 已经积累了丰富的经验，能够设计精致的知识图谱，并进行针对性增强，确保数据的准确性和实用性​ (Analytics India Magazine)​。

此外，GPT-4o mini 被设计为一种高效的逻辑驱动器，尽管它在回答百科全书式的问题时可能表现平平，但它在网络搜索和微调等任务中展现出了巨大的潜力。合成数据的使用使得小模型能够更好地识别提示中的合理性，找到内在规律，从而在特定应用中提供精准的结果​ (Analytics India Magazine)​​ (AOL.com)​。

综上所述，GPT-4o mini 的设计不仅注重规模的优化，更强调数据质量和应用场景的适配，代表了小型 AI 模型未来发展的重要方向。
"""

# Split the source text
text_splitter = CharacterTextSplitter()
texts = text_splitter.split_text(source_text)

 # Create Document objects for the texts (max 3 pages)
docs = [Document(page_content=t) for t in texts[:3]]

llm = ChatOpenAI(temperature=0, model="gpt-4o")
chain = load_summarize_chain(llm, chain_type="map_reduce")
summary = chain.invoke(docs)
print("----------text summary----------")
print(summary)
