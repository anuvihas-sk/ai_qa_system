from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_llm(document_text, question):

    prompt = f"""
You are a helpful PDF question-answering assistant.

Answer the question using ONLY the information
provided in the document.

If the answer is not present in the document, say:
"I could not find the answer in the document."

Document:
{document_text}

Question:
{question}

Answer:
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text