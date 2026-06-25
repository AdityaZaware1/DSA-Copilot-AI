
import os

from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

dir = 'db'

def get_embeddigs():

    return HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

def create_vector_store():

    embeddings = get_embeddigs()

    if os.path.exists(dir):

        return Chroma(
            persist_directory=dir,
            embedding_function=embeddings
        )
        

    loader = PyPDFLoader("/DsaSolution.pdf")

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100)

    texts = text_splitter.split_documents(documents)

    vectorstore = Chroma.from_documents(
        texts, 
        embeddings, 
        persist_directory=dir)

    vectorstore.persist()
