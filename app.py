import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # load .env if present

API_KEY = os.getenv("MISTRAL_API_KEY")
MODEL = "mistral-large"

st.set_page_config(page_title="Trading AI Bot", layout="wide")

st.title("Trading AI Bot (Mistral Large)")

if not API_KEY:
    st.error(
        "MISTRAL_API_KEY is not set.\n\n" 
        "Create a `.env` file with `MISTRAL_API_KEY=your_key` or set the environment variable.")
    st.stop()

st.markdown(
    """
    This app uses Mistral's `mistral-large` model to generate **trade ideas** based on a symbol and a short prompt.

    > Note: This is a demo. Always validate any trading idea before acting on it.
    """
)

with st.sidebar:
    st.header("Inputs")
    symbol = st.text_input("Ticker / Symbol", value="AAPL")
    timeframe = st.selectbox("Timeframe", ["1d", "1h", "4h", "1w"], index=0)
    context = st.text_area(
        "Context / Notes",
        value=(
            "You are a professional stock trader. Provide a short technical analysis,"
            " a trade suggestion (buy/sell/hold), a target price, and a stop loss."
        ),
        height=120,
    )
    max_tokens = st.slider("Max tokens", min_value=100, max_value=800, value=300)

st.subheader("Trade Idea")

if st.button("Generate Trade Insight"):
    prompt = (
        f"Symbol: {symbol}\n"
        f"Timeframe: {timeframe}\n"
        f"Context: {context}\n"
        "Provide a concise trading idea with reasoning, an actionable recommendation,"
        " and suggested risk management parameters."
    )

    with st.spinner("Asking Mistral..."):
        try:
            output = call_mistral(prompt, max_tokens=max_tokens)
            st.markdown("**Mistral response:**")
            st.code(output.strip())
        except Exception as exc:
            st.error(f"Request failed: {exc}")


def call_mistral(prompt: str, max_tokens: int = 300) -> str:
    """Call Mistral API (mistral-large) to generate text."""
    url = f"https://api.mistral.ai/v1/models/{MODEL}/generate"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_tokens,
            "temperature": 0.55,
            "top_p": 0.9,
        },
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    # The Mistral API typically returns a dict with `results` where each item has `output`.
    if isinstance(data, dict) and "results" in data and data["results"]:
        result = data["results"][0]
        if isinstance(result, dict):
            return result.get("output", str(result))
        return str(result)

    # Fallback: return full JSON
    return str(data)
