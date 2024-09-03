from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307")

prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are a comedian Who tells a joke about person named Anson along with the {topic}."),
    ("human","Tell me {joke_count} jokes."),
])

format_prompt = RunnableLambda(lambda x:prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x:model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

response = chain.invoke({"topic":"Computer","joke_count":3})

print(response)