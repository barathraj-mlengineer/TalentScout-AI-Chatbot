def get_question_prompt(tech_stack):
    return f"""
You are a technical interviewer. A candidate has declared their tech stack as: {tech_stack}.
Generate 3-5 relevant, intermediate-to-advanced level technical questions for EACH item in the stack.
Make sure the questions test real-world understanding and problem-solving skills. Return only the questions.
"""