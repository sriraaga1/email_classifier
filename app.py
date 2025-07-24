import streamlit as st
from dotenv import load_dotenv
import os
import requests

# Load your .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


st.set_page_config(page_title="📩 Email Classifier Bot")
st.title("📩 Email Classifier Bot")

# Input fields
subject = st.text_input("Email Subject")
body = st.text_area("Email Body")

# Button click
if st.button("Classify Email"):
    if not API_KEY:
        st.error("❌ API key not found. Please check your .env file.")
    else:
        prompt = f"""
You are an expert email classifier.

Read the following email and do two things:
1. Classify the email into one of the three types: New Order, Order Issue, Order Feedback
2. Extract key attributes that would help the support team

Subject: {subject}
Body: {body}

Return output in this format:
Class: <one of 3 types>
Attributes: <list key details like product, issue, etc.>
"""

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://email-classifier.local",  # required for OpenRouter
            "X-Title": "email-classifier-bot"
        }

        data = {
            "model": "deepseek/deepseek-r1-0528:free",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )

        try:
            result = response.json()
            if "choices" in result:
                output = result["choices"][0]["message"]["content"]
                st.success("✅ Classification Complete!")
                st.markdown(f"**Output:**\n\n{output}")
            else:
                st.error("⚠️ Unexpected response (no 'choices' field):")
                st.json(result)
        except Exception as e:
            st.error("❌ Something went wrong.")
            st.text(str(e))
