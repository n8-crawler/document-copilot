from app.retrieval.retriever import Retriver
from app.llm.prompt import PromptBuilder
from app.embeddings.generator import EmbeddingGenerator
from app.llm.generator import Llmgenerator
from app.database import sessionlocal
def llm_pipeline(user_query:str):
    db = sessionlocal()
    embeddings = EmbeddingGenerator().generate_embeddings(user_query)
    print('THINKING....embedding')

    retriver = Retriver(db=db).retrive(query_embedding=embeddings)
    print('THINKING...finding matches')
    
    prompt = PromptBuilder().build_prompt(user_question=user_query,chunk_list = retriver,chat_history=None)
    print('THINKING....creating prompt')
    message = Llmgenerator().generate(prompt=prompt)
    print("=" * 80)
    print(f'HERE WHAT I FOUND: {message} ')
    db.close()

if __name__ == "__main__":
    question = input()
    llm_pipeline(user_query=question)




