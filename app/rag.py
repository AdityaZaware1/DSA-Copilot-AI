
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

import prompt
import llm

embeddings = HuggingFaceEmbeddings(
    model = 'sentence-transformers/all-MiniLM-L6-v2'
)

vectorstore = Chroma(
    persist_directory='db',
    embedding_function=embeddings
)

retriver = vectorstore.as_retriever(search_kwargs={"k": 3})

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

def rag_pipeline(query, language):

    docs = retriver.invoke(query)

    context = format_docs(docs)

    final_prompt = prompt.prompt.format(
        context=context,
        question=query,
        language=language
    )

    return llm.call_llm(final_prompt)

