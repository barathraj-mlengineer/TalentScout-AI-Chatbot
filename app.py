import streamlit as st
from utils import generate_questions

st.set_page_config(page_title="TalentScout AI Chatbot", layout="centered")

st.title("🤖 TalentScout - AI Hiring Assistant")
st.markdown("Welcome to TalentScout! I’ll help gather your info and ask tech questions based on your skills.")

# Collect Candidate Info
with st.form("candidate_form"):
    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email Address")
    phone = st.text_input("📞 Phone Number")
    experience = st.number_input("🧠 Years of Experience", min_value=0, max_value=50,value=0)
    location = st.text_input("📍 Current Location")
    position = st.text_input("💼 Desired Position(s)")
    tech_stack = st.text_area("🛠️ Tech Stack (e.g., Python, Django, React, MySQL)")

    submit = st.form_submit_button("🚀 Generate Technical Questions")

# Generate Questions
if submit:
    if all([name, email, phone, experience, location, position, tech_stack]):
        st.info("⏳ Generating questions using LLaMA3 via Groq API...")
        questions = generate_questions(tech_stack)
        st.success("✅ Here are your custom questions:")
        for i, q in enumerate(questions, 1):
            st.markdown(f"**Q{i}.** {q}")
    else:
        st.warning("⚠️ Please fill out all fields before submitting.")

# End Conversation Button
if st.button("❌ End Conversation"):
    st.write("Thank you for interacting with TalentScout. We’ll reach out to you soon! 👋")
    st.stop()