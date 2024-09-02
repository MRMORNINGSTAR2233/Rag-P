from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307")

chat_history =[]

sysmes = SystemMessage(content="You are my personal coder.")
chat_history.append(sysmes)

while True:
    query = input("You:")
    if query.lower()=="exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    print("AI:", response)

print("---Message History---")
print(chat_history)