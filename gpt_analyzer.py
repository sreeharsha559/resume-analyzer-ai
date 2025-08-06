import requests
import os

# Set your OpenRouter API key in an environment variable or paste directly
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Or paste your key as a string
if not OPENROUTER_API_KEY:
    OPENROUTER_API_KEY = "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"  # Replace with your real key

# Define the API endpoint
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Choose a model available on OpenRouter (can also try `openai/gpt-3.5-turbo` or `openai/gpt-4`)
MODEL ="mistralai/mixtral-8x7b-instruct"



def analyze_resume_with_gpt(resume_text):
    # your code
  # <-- This must match!
    ...

    prompt = f"""
    You are an expert career consultant. Analyze the following resume and give detailed feedback:
    - Skills that are strong
    - Skills missing for a software developer role
    - Suggestions to improve
    - Improvements to the formatting and content

    Resume Text:
    {resume_text}
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant specialized in resume reviewing."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=body)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"
