from gpt4all import GPT4All
from pathlib import Path
import os
import bs4

from langchain_openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain import hub
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

print("Loading model")
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

mydir = Path.home() / 'workspace' / 'RAG-builder' / 'genTexts'
print("Loading directory", mydir)
loader = DirectoryLoader(mydir.absolute(), glob="**/*.txt")
print("Instantiated loader")
data = loader.load()

print("Data loaded")
print("Splitting text and embedding using GPT4All embeddings")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(data)
vectorstore = Chroma.from_documents(documents=splits, embedding=GPT4AllEmbeddings())

print("Finished the vectorstore setup")
# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
llm = client

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def enter_question():
    print("About to invoke the RAG chain")
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    question = input("Enter your prompt: ")
    for chunk in rag_chain.stream(question):
        print(chunk, end="", flush=True)
    print("Just finished invoking the RAG chain")

try:
    while True:
        enter_question()
except KeyboardInterrupt:
    print("Exiting...")

vectorstore.delete_collection()
