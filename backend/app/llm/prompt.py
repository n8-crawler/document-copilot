from app.retrieval.pipeline import retrieval_pipeline
from app.models.documentchunks import DocumentChunk
class PromptBuilder:
    def context(self,user_question:str,chunk_list :list[DocumentChunk]):
        context_text = ""
        for index,chunk in enumerate(chunk_list):
            context_text +=(
                f"context {index} \n"
                f"ticker : {chunk.document_chunk.ticker}\n"
                f"form : {chunk.document_chunk.form}\n"
                f"filing date : {chunk.document_chunk.filing_date}\n"
                f"source : {chunk.document_chunk.source_url}\n"
                f"{chunk.content}\n\n"
                f"{'=' * 50}\n\n"
            )
    
        prompt = f"""

                You are an expert financial analyst specializing in SEC filings.

                Use ONLY the provided context to answer the user's question.

                Instructions:

                - Answer only from the supplied context.

                - Do not make up facts.

                - If the answer cannot be found, reply:

                "I don't have enough information in the provided documents."

                - Keep the answer concise but complete.

                - When appropriate, mention which filing the information came from.

                - If user asks for evidence of data u can provide the source url.

                Context:

                {context_text}

                Question:

                {user_question}

                Answer:

            """
        return prompt.strip()





    
