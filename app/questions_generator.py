
import llm

def generate_question(topic, difficulty, language):

    prompt = f"""
    You are an expert DSA interviewer.

    Generate ONE unique DSA problem.

    Topic: {topic}
    Difficulty: {difficulty}

    Give output in this format:

    1. Problem Title
    2. Problem Statement
    3. Constraints
    4. Example Input/Output
    5. Hints
    6. Expected Time Complexity
    7. Starter Code in {language}

    Make problem interview-level.
    Do not copy famous LeetCode questions exactly.
    """

    response = llm.call_llm(prompt)

    return response

