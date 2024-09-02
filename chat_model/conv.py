from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307")


messages =[
    SystemMessage(content="Solve the math problem",),
    HumanMessage(content="what is tan(45)+cos(45)?"),
]
result = model.invoke(messages)
print("Answer from AI is: ",{result.content})


messages =[
    SystemMessage(content="Solve the math problem",),
    HumanMessage(content="what is 2+2?"),
    AIMessage(content="4"),
    HumanMessage(content="what is 4+2?")
]
result = model.invoke(messages)
print("Answer from AI is: ",{result.content})