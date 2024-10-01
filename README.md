# Desktop-Search-App

## Introduction
The Desktop Search Application is a Python tool that uses Natural Language Processing (NLP) and Large Language Models (LLMs) to interpret user queries and search through files for relevant content and metadata.

## Features
- Natural Language Query Interpretation
- Content and Metadata Retrieval
- Multi-format Support (.txt, .pdf, .docx)
- User-friendly GUI with PyQt5
- Efficient Search using vector stores

## Project Structure
```
├── desktop_search_app.py 
├── file_processing.py 
├── indexing.py 
├── vector_store.py 
├── requirements.txt 
├── indexed_files.json 
└── README.md
```


## Prerequisites
- Python 3.7 or higher
- OpenAI API Key
- Required Python Libraries: `langchain`, `openai`, `PyPDF2`, `python-docx`, `PyQt5`

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/desktop-search-application.git
    cd desktop-search-application
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the OpenAI API key:
    ```bash
    export OPENAI_API_KEY='your_openai_api_key'  # On Windows use `set OPENAI_API_KEY=your_openai_api_key`
    ```

## Usage
1. Run the application:
    ```bash
    python desktop_search_app.py
    ```

2. Use the GUI to enter your query and view search results.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- LangChain
- OpenAI
- PyPDF2
- python-docx
- PyQt5
