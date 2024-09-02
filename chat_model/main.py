from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307")

result = model.invoke("How many letters are there in English alphabet?")
print("Full Result")
print(result)
print("content:")
print(result.content)