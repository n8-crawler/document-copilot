from langgraph.graph import StateGraph,START,END
from app.graph.state import ChatState
from app.graph.nodes import getthread,create_user_message,generate_embeddings,retrive_chunks,chat_history,create_prompt,llm_response,save_ai_message

# this will make the sequential orchestration of nodes like in did in chatservice.py but here i will use stategraph to do that and also i will use state object to pass data between nodes

builder = StateGraph(ChatState)

#create sequence of execution
builder.add_sequence([
    ("thread",getthread),
    ("user message",create_user_message),
    ("generate embeddings",generate_embeddings),
    ("retrive chunks",retrive_chunks),
    ("chat history",chat_history),
    ("create prompt",create_prompt),
    ("LLM response",llm_response),
    ("save AI message",save_ai_message),
])

builder.add_edge(START,"thread")
builder.add_edge("save AI message",END)

chat_graph = builder.compile()