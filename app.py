from dotenv import load_dotenv

from pdf_reader import extract_text_from_pdf
from llm import ask_llm

load_dotenv()

PDF_PATH = "sample.pdf"

print("Reading PDF...")

document_text = extract_text_from_pdf(PDF_PATH)

print("PDF loaded successfully!")
print("PDF Q&A is ready!")

while True:

    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    answer = ask_llm(document_text, question)

    print("\nAnswer:")
    print(answer)