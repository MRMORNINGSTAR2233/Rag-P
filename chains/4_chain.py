from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307")

prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are an expert product reviewer ."),
    ("human","List the main features of the product {product_names}."),
])

def analyse_pros(features):
    pros_template = ChatPromptTemplate.from_messages([
        ("system","You are an expert product reviewer ."),
        ("human",
         "Gien these features:{features}, list the pros these features.",),
    ])
    return pros_template.format_prompt(features = features)


def analyse_cons(features):
    cons_template = ChatPromptTemplate.from_messages([
        ("system","You are an expert product reviewer ."),
        ("human",
         "Gien these features:{features}, list the cons these features.",),
    ])
    return cons_template.format_prompt(features = features)



def combine_pros_cons(pros,cons):
    return f"Pros:\n{pros}\n\nCons:\n{cons}"



pros_branch_chain =(\
    RunnableLambda(lambda x: analyse_pros(x))|model|StrOutputParser())

cons_branch_chain = (
    RunnableLambda(lambda x: analyse_cons(x))|model|StrOutputParser())

chain = (
    prompt_template
    |model
    |StrOutputParser()
    |RunnableParallel(branches = {"pros":pros_branch_chain,"cons":cons_branch_chain})
    |RunnableLambda(lambda x : combine_pros_cons[x["branches"]["pros"],x["branches"]["cons"]])
)

result = chain.invoke({"prodcut_name:","MacBook Pro"})
print(result)