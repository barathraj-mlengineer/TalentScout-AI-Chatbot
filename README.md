# 🧠 TalentScout AI Hiring Assistant

This is an AI-powered chatbot built with **Streamlit** and **Groq's LLaMA3** models. It collects candidate details and generates personalized technical questions for initial hiring screenings.

## 🚀 Features

- Collects full candidate info
- Dynamic question generation based on tech stack
- Streamlit-based user interface
- Uses LLaMA3 via Groq API
- Local or cloud deployment ready

## 🛠️ Setup

```bash
git clone https://github.com/yourname/talentscout-chatbot
cd talentscout-chatbot
pip install -r requirements.txt
cp .env.example .env
# Add your Groq API key in .env
streamlit run app.py
```

## 🌐 Deployment

- Deploy on Streamlit Cloud or Render
- Keep `.env` secure