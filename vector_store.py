from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def create_vector_store(indexed_files):
    texts = [doc['content'] for doc in indexed_files]
    metadatas = [doc['metadata'] for doc in indexed_files]
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
    return vector_store

def create_retrieval_chain(vector_store):
    llm = OpenAI(temperature=0)
    retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=vector_store.as_retriever()
    )
    return retrieval_chain
