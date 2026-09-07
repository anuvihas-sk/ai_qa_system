import json
import urllib.request


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

    data = json.dumps({
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }).encode("utf-8")

    request = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["response"]