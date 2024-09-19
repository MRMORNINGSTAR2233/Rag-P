from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain.schema.runnable import RunnableLambda


load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307")

prompt_template = ChatPromptTemplate.from_messages([
    ("system","You teare a comedian who tells jokes about {topic}."),
    ("human","Tell me a {joke_count} jokes."),
])

uppercase_about = RunnableLambda(lambda x :x.upper())
count_words = RunnableLambda(lambda x : f"{len(x.split())}\n{x}")

chain = prompt_template|model|StrOutputParser()|uppercase_about|count_words

result = chain.invoke({"topic":"layers","joke_count":3})

print(result)