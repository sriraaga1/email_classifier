# 📩 Email Classifier Bot

This is a simple Streamlit web app that helps classify customer emails into one of the following categories:

- 🆕 New Order  
- ❌ Order Issue  
- 💬 Order Feedback

It also extracts useful information like product name, issue type, and more to help the support team handle emails faster.

---

## 🔧 How It Works

1. Enter the **subject** and **body** of the email.
2. The app uses a GenAI model (via API) to:
   - Classify the email.
   - Extract key details from the text.

---

## 🛠️ Built With

- Python 🐍  
- Streamlit 📊  
- dotenv 🔐 (to store API key securely)  
- OpenRouter API (or OpenAI-compatible)

---

## 💻 How to Run It Locally

1. Clone this repo  
2. Install requirements:
   ```bash
   pip install -r requirements.txt
3. Add your API key to a .env file like this:
   API_KEY=your_api_key_here
4. Run the app:
   streamlit run app.py

📌 Notes
The .env file is ignored in GitHub using .gitignore to keep your API key safe.

This is a basic project for learning and experimenting with Generative AI and Streamlit.
