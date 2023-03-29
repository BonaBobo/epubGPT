"""main.py."""
import os

import gradio as gr
from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, download_loader

load_dotenv()

book = "../book/Glucose_revolution.epub"
openai_api_key = os.environ.get("OPENAI_API_KEY")


def predict(query: str) -> str:
    """
    Predict function for the chatbot.

    :param input: input question for the chatbot
    :type input: string
    :return: response of the query
    :rtype: string
    """
    response = index.query(query, similarity_top_k=1)
    return response


if __name__ == "__main__":
    EpubReader = download_loader("EpubReader")

    title = "Chat with the Glucose Goddess 🧜‍♀️"
    loader = EpubReader()
    documents = loader.load_data(file=book)

    index = GPTSimpleVectorIndex(documents)

    gr.Interface(fn=predict, title=title, inputs=["text"], outputs=["text"]).launch(share=False)
