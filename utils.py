import requests
from prompts import get_question_prompt

# --- HARD-CODED SETTINGS ---------------------------------
GROQ_API_KEY = "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"     # ← put your key
GROQ_MODEL    = "llama3-70b-8192"                  # ← or whatever model you’re using
# ---------------------------------------------------------

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
            {"role": "user",   "content": get_question_prompt(tech_stack)}
        ],
        "temperature": 0.7,
        "max_tokens": 700
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        # split lines that begin with “- ” or similar list markers
        questions = [q.lstrip("-•").strip() for q in content.splitlines() if q.strip()]
        return questions
    else:
        return [f"Error: {response.status_code} - {response.text}"]
