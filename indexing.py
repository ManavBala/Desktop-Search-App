import os
import json
from file_processing import extract_text, get_metadata

def index_files(directory):
    indexed_files = []
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                content = extract_text(file_path)
                metadata = get_metadata(file_path)
                indexed_files.append({'content': content, 'metadata': metadata})
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    with open('indexed_files.json', 'w', encoding='utf-8') as f:
        json.dump(indexed_files, f, ensure_ascii=False, indent=4)
    return indexed_files
