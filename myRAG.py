from langchain_openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain import hub
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from pathlib import Path

# Setup local LLM client
client = OpenAI(base_url="http://localhost:1234/v1")

# Define the directories for loading and processing documents
mydir = Path.home() / 'workspace' / 'RAG-experiments' / 'genTexts'
print("Loading directory", mydir)

# Load and process documents
loader = DirectoryLoader(mydir.absolute(), glob="**/*.txt")
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(data)

# Create vector storage for embeddings
vectorstore = Chroma.from_documents(documents=splits, embedding=GPT4AllEmbeddings())

# Setup retriever and prompt
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

# Define a more specific context for financial analysis
context_prefix = """
Context for Financial Analysts: This system is designed to support financial analysts specializing in macroeconomics. 
Analysts are tasked with evaluating current interest rates and predicting future economic conditions to formulate 
robust investment strategies. They rely heavily on quantitative models to extrapolate trends from historical data and 
interpret complex economic reports. Key considerations include GDP growth rates, inflation forecasts, and global 
economic indicators that influence market dynamics. This analysis helps in making data-driven decisions to optimize 
portfolio performance under varying economic scenarios.
"""

# Format docs for output
def format_docs(docs):
    # Include the specialized context at the beginning of the document content
    return context_prefix + "\n\n" + "\n\n".join(doc.page_content for doc in docs)

def enter_question():
    # Welcome and instructional message
    welcome_message = """
    Welcome to the Financial Analysis RAG System! This interactive session is designed to assist financial analysts in assessing macroeconomic conditions. 
    Please feel free to ask any questions related to interest rates, investment strategies, economic forecasts, and other macroeconomic concerns. 
    Our system uses a comprehensive corpus of economic documents to provide you with informed responses. Type 'exit' to end the session.
    """
    print(welcome_message)
    
    print("Enter your prompt, or type 'exit' to quit:")
    while True:
        question = input("> ")
        if question.lower() == 'exit':
            break

        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | client
            | StrOutputParser()
        )

        for chunk in rag_chain.stream(question):
            print(chunk, end="", flush=True)
        print()

# Main program
if __name__ == "__main__":
    try:
        enter_question()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        vectorstore.delete_collection()
