import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"

def call_llm(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 180
    }
}


    res = requests.post(OLLAMA_URL, json=payload, timeout=120)
    res.raise_for_status()

    return res.json()["response"].strip()
