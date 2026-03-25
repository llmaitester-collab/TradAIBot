# Trading AI Bot (Mistral Large)

A simple Streamlit demo that uses **Mistral AI's `mistral-large`** model to generate trading ideas.

## 🚀 Setup

1) Ensure your virtual environment is activated (you already have `.venv`):

```powershell
.\.venv\Scripts\Activate
```

2) Install dependencies:

```powershell
pip install -r requirements.txt
```

3) Set your API key (do not commit this key to version control):

```powershell
setx MISTRAL_API_KEY "pInZWCMLPJaABBnfrTwXsufHz1oqs0X5"
```

Alternatively, create a `.env` file at the repo root containing:

```
MISTRAL_API_KEY=pInZWCMLPJaABBnfrTwXsufHz1oqs0X5
```

### 🛰️ Streamlit Cloud / Streamlit Community Deployment
If you deploy this app to Streamlit Cloud, add the key as a secret:

1. Open your Streamlit app settings.
2. Go to **Secrets**.
3. Add:

```
MISTRAL_API_KEY = "eHPEqOB8AHtV5SHAXJNM8ZxWOWVqVVkJ"
```

## ▶️ Run the app

```powershell
streamlit run app.py
```

Then open the browser at:

- **Local URL:** http://localhost:8501

## 🧠 How it works

- The app builds a prompt from the UI inputs.
- It calls the Mistral API (`mistral-large`) to generate a trade idea.
- The response is displayed in the UI.

> ⚠️ This is a demo. Never trade real money based on AI output without your own verification.
