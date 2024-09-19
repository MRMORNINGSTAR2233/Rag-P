from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableBranch
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatPromptTemplate(model = "claude-3-haiku-20240307")

posi_feedback_template = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assitant."),
    ("human",
     "Generate a thank you note for this positive feedback:{feedback}."),
])

negi_feedback_template = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant."),
    ("human",
     "Generate a request for more details for this negative feedback:{feedback}."),
])

neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a request for more details for this neutral feedback: {feedback}.",
        ),
    ]
)

escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a message to escalate this feedback to a human agent: {feedback}.",
        ),
    ]
)

# Define the feedback classification template
classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}."),
    ]
)



branches = RunnableBranch(
    (
        lambda x: "positive" in x,
        posi_feedback_template|model|StrOutputParser()
    ),
     (
        lambda x: "negative" in x,
        negi_feedback_template | model | StrOutputParser()  # Negative feedback chain
    ),
    (
        lambda x: "neutral" in x,
        neutral_feedback_template | model | StrOutputParser()  # Neutral feedback chain
    ),
    escalate_feedback_template | model | StrOutputParser()

)


classification_chain = classification_template|model|StrOutputParser()|branches
chain = classification_chain|branches


review = "The product is terrible. It broke after just one use and the quality is very poor."
result = chain.invoke({"feedback":review})

print(result)