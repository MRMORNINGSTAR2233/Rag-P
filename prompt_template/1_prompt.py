from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

template = "Tell me a joke about {topic}"
prompt_template =ChatPromptTemplate.from_temaplate(template)

print("----Prompt From Template----")
prompt=prompt_template.invoke({"topic":"chicken"})
print(prompt)