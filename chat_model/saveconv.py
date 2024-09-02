from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from google.auth import compute_engine
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory

load_dotenv()

model = ChatAnthropic(model="claude-3-haiku-20240307")

PROJECT_ID = ""
SESSION_ID = ""
COLLECTION_NAME = ""


print("initializing Firestore client")
client = firestore.Client(project=PROJECT_ID)

print("initializing Firestore Chat History...")
chat_history = FirestoreChatMessageHistory(
    client=client, collection_name=COLLECTION_NAME, session_id=SESSION_ID
)

print("Chat history initializeed")
print("Current Chat History:", chat_history.messages)


print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    query=input("User")
    if query.lower()=='exit':
        break
    chat_history.add_user_message(query)

    result = model.invoke(chat_history.messages)
    chat_history.add_ai_message(result.content)

    print("AI:{result.content}")