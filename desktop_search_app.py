import sys
import os
from dotenv import load_dotenv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton
)
from indexing import index_files
from vector_store import create_vector_store, create_retrieval_chain

# Load environment variables
load_dotenv()

class DesktopSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Desktop Search Application')
        self.resize(600, 400)
        self.indexed_files = []
        self.vector_store = None
        self.retrieval_chain = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.query_label = QLabel('Enter your query:')
        layout.addWidget(self.query_label)

        self.query_input = QLineEdit()
        layout.addWidget(self.query_input)

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.perform_search)
        layout.addWidget(self.search_button)

        self.results = QTextEdit()
        self.results.setReadOnly(True)
        layout.addWidget(self.results)

        self.setLayout(layout)

    def load_index(self):
        import json
        if os.path.exists('indexed_files.json'):
            with open('indexed_files.json', 'r', encoding='utf-8') as f:
                self.indexed_files = json.load(f)
        else:
            directory = os.environ.get('SEARCH_DIRECTORY')
            if not directory:
                raise ValueError("The SEARCH_DIRECTORY environment variable is not set.")
            self.indexed_files = index_files(directory)
        self.vector_store = create_vector_store(self.indexed_files)
        self.retrieval_chain = create_retrieval_chain(self.vector_store)

    def perform_search(self):
        query = self.query_input.text()
        if not self.retrieval_chain:
            self.load_index()
        try:
            response = self.retrieval_chain.run(query)
            self.results.setText(response)
        except Exception as e:
            self.results.setText(f"Error: {e}")

def main():
    app = QApplication(sys.argv)
    window = DesktopSearchApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
