from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate 

load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307")

# print("----Prompt from Template----")
# template = "Tell me a joke about{topic}."
# prompt_template = ChatPromptTemplate.from_template(template)

# prompt = prompt_template.invoke({"topic":"cat"})
# result = model.invoke(prompt)
# print(result.content)

print("----Prompt With Multiple Template ---\n")
template_multiple = """you are a helpful assistant.
Human:Tell me a {adjective} short story about (animal).
Assistant:"""

prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective":"funny","animal":"panda"})
result=model.invoke(prompt)
print(result.content)