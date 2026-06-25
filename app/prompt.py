
from langchain_core.prompts import PromptTemplate

template = """
You are a DSA expert.

Use the provided context to answer the question.

Context:
{context}

Question:
{question}

Give answer in this format:
1. Intuition
2. Approach
3. Code langeuage = {language}
4. Complexity
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question", "language"]
)