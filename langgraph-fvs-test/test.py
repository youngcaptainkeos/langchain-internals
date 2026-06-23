from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="qwen/qwen3-8b",
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

response = llm.invoke("What is 2+2?")

print(response.content)