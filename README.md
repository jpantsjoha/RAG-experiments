
# Retrieval-Augmented Generation (RAG) Setup with Local, Privately Hosted LLM 

## RAG Intention 

**To operate as a local Financial Macro Analyst on your PDF Research Corpus**

- **Drop PDFs**

- **Run RAG & Ask Questions**


## About
This repo came about at the back of my recent all-things GenerativeAI hands-on explorations followed by the cross-training into Machine Learning for a deeper understanding on this subject matter.
I have "preached" the [need for rapid upskilling](https://www.linkedin.com/pulse/need-frequent-upskill-age-genai-jaroslav-pantsjoha/?trackingId=ifjzoG1VQTi0CHVHRIwKGg%3D%3D) and indeed documented my own [#PersonalDevelopment journey here](https://jaroslav-pantsjoha.medium.com/google-cloud-machine-learning-exam-prep-broken-down-by-learning-effort-levels-21f96088a274). 
This repo will eventually grow a collection of my hands-on accelerators. 

Tag along and follow this journey on [Linkedin](https://www.linkedin.com/in/johas/) and [Medium Blog](https://jaroslav-pantsjoha.medium.com/)  

### Assumptions on Levels of Knowledge Required, Implied
- The Key emphasis for this experiment is to get this running quickly, and operating locally soon as - **Most Value for Least Effort**
- My Experience: My Background is in Application Modernisation, GitOps & Kubernetes - as a Container Platform and Google Cloud evangelist. I'm not necessarily a developer day-in day out. And that's fine. So I will rely on GenAI to help me accelerate this [experimentation journey as I have done in the past](https://github.com/jpantsjoha/PromptKeeper-GenAI-Prompts).
- My Tools: I have started the easy way, and using [LM Studio](https://lmstudio.ai/) that allowed me to hot-swap LLMs and compare for different use cases, and purposes. I have started with this to get my experimenting with LLMs for local use.


## RAG Project Description
This project implements a Retrieval-Augmented Generation (RAG) system that leverages the power of local Large Language Models (LLMs) to enhance the process of generating responses based on the retrieval of relevant documents. The system reads multiple text files from a specified directory, processes these files to retrieve contextually relevant information, and uses this information to generate enhanced responses to user queries. Inspired by Ruddy Thor [Rag Demo](https://github.com/ruddythor/mick.ai)

![RAG Demo Screenshot](RAG-demo-screenshot.png)

## RAG Features
- **Multiple File Reading:** Efficiently processes multiple text files for dynamic content retrieval.
- **Advanced Text Processing:** Utilizes `RecursiveCharacterTextSplitter` for optimal text manipulation and embedding.
- **Local LLM Support:** Fully compatible with local LLM endpoints to minimize dependency on external APIs.
- **Interactive Query System:** Live user interface for real-time querying and response generation.


## RAG Architecture
The system architecture is outlined in the diagram below. It showcases the flow from document loading and processing to response generation, facilitated by the interplay between various components.

![RAG Architecture](rag_architecture.png)

## New Feature: Prompt Context Window
The Prompt Context Window is a crucial enhancement in our RAG setup. It allows users to predefine a specific context that is automatically prepended to each query. This context acts as a primer, setting the stage for the LLM to generate more focused and relevant responses based on predefined background information. 

### Current Context Window Implementation
```
# Define a more specific context for financial analysis
context_prefix = """
Context for Financial Analysts: This system is designed to support financial analysts specializing in macroeconomics. 
Analysts are tasked with evaluating current interest rates and predicting future economic conditions to formulate 
robust investment strategies. They rely heavily on quantitative models to extrapolate trends from historical data and 
interpret complex economic reports. Key considerations include GDP growth rates, inflation forecasts, and global 
economic indicators that influence market dynamics. This analysis helps in making data-driven decisions to optimize 
portfolio performance under varying economic scenarios.
"""
```

### Benefits:
- **Increased Relevance**: Ensures that the LLM's responses are more aligned with the user's expectations and the specific domain of inquiry, such as financial analysis or economic forecasting.
- **Enhanced Accuracy**: By providing a consistent contextual backdrop, the model can better understand and interpret the user's queries, leading to more accurate and insightful responses.
- **Customization**: Users can tailor the context to fit various themes or projects, making this tool adaptable across different professional fields and research areas.


## RAG Architecture Details
The architecture consists of several key components:
- **Directory Loader:** Manages the ingestion of text files from designated directories.
- **Text Splitter:** Breaks down large documents into manageable chunks.
- **GPT4All Embeddings:** Converts text into meaningful embeddings.
- **Chroma Vector Store:** Handles the storage and retrieval of embeddings.
- **OpenAI LLM Client:** Facilitates communication with the LLM for generating responses.
- **RAG Chain:** Orchestrates the flow from retrieval to response generation.


### How do you Get Started - Quick and Easy
1. Clone the repository to your local machine.
2. Ensure you have a local LLM endpoint running at `http://localhost:1234/v1`.
3. Install the required Python libraries listed in **below**
4. Put your PDF (Data Corpus/Reasearch) into **PDFs** folder and run `python convert-to-text.py` 
5. Then, run the main script to start the RAG process: `python myRAG.py`.
5. Enter prompts as required to retrieve and generate responses.

### Dependencies
- Python 3.8+
- gpt4all
- langchain_openai
- bs4
- pathlib

# Installation Guide

Before running the RAG setup, you need to install several dependencies, which include Python packages and system libraries. Follow the steps below to install them on your system.

## Prerequisites
Ensure you have Python 3.8+ and pip installed on your system. You can check your Python version with:

```sh
python --version
```

If you're using a Mac, you'll also need Homebrew to install some of the system dependencies:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## System Dependencies
Certain components require system-level dependencies like poppler for PDF processing and graphviz for generating visual representations of the architecture.

### macOS
```sh
brew install poppler pkg-config python graphviz
```

### Python Packages
The following Python packages are required. You can install them using pip:

```sh
pip install open-interpreter bs4 langchain-community langchain-chroma langchain langchainhub gpt4all pdftotext PyMuPDF langchain_openai unstructured pygraphviz
```

To handle any potential issues with the pygraphviz installation related to library paths, you can also install it using the following commands:

```sh
pip install pygraphviz --install-option="--include-path=/usr/local/include/graphviz" --install-option="--library-path=/usr/local/lib/graphviz/"
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributors are welcome to propose enhancements, fix bugs, or improve documentation. Please feel free to fork the repository and submit pull requests.
