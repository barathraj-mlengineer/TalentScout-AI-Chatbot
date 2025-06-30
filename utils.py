import requests
import os
from prompts import get_question_prompt
from dotenv import load_dotenv

load_dotenv()


def generate_questions(tech_stack):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert AI hiring assistant."},
            {"role": "user", "content": get_question_prompt(tech_stack)}
        ],
        "temperature": 0.7,
        "max_tokens": 700
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        content = response.json()['choices'][0]['message']['content']
        questions = [q.strip("- ").strip() for q in content.strip().split("\n") if q.strip()]
        return questions
    else:
        return [f"Error: {response.status_code} - {response.text}"]