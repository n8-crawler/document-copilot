from langgraph.graph import StateGraph,START,END
from app.graph.state import ChatState
from app.graph.nodes import getthread,create_user_message,generate_embeddings,retrive_chunks,chat_history,create_prompt,llm_response,save_ai_message

# this will make the sequential orchestration of nodes like in did in chatservice.py but here i will use stategraph to do that and also i will use state object to pass data between nodes

builder = StateGraph(ChatState)
# registering the nodes
builder.add_node("thread",getthread)
builder.add_node("user message",create_user_message)
builder.add_node("generate embeddings",generate_embeddings)
builder.add_node("retrive chunks",retrive_chunks)
builder.add_node("chat history",chat_history)
builder.add_node("create prompt",create_prompt)
builder.add_node("LLM response",llm_response)
builder.add_node("save AI message",save_ai_message)
#create sequence of execution
builder.add_sequence([
    "thread",
    "user message",
    "generate embeddings",
    "retrive chunks",
    "chat history",
    "create prompt",
    "LLM response",
    "save AI message"
])

builder.add_edge(START,"thread")
builder.add_edge("save AI message",END)

chat_graph = builder.compile()