from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307")

prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are my a comedian who tells jokes about {topic}."),
    ("human","Tell me {joke_count} jokes"),
])

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic":"Anson","joke_count":3})

print(result)