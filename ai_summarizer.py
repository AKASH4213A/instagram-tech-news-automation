import json

def summarize_article(article, llm_call):
    prompt = f"""
You are a tech news analyst.

TASK:
Extract information from the news and return ONLY valid JSON.

JSON FORMAT (must follow exactly):
{{
  "kya_hua": "1–2 short factual sentences explaining what happened",
  "kyun_important": "2–3 clear sentences explaining impact, consequences, or why readers should care"
}}

IMPORTANT RULES:
- Both fields MUST be non-empty
- Do NOT include words like Headline, Kya hua, Kyun important
- Do NOT add extra keys
- Do NOT add explanations
- Output ONLY the JSON object
- The 'kyun_important' field MUST be more detailed than 'kya_hua'
- Use the full space to explain impact or implications


STYLE GUIDANCE:
- Avoid generic phrases like "raises awareness" or "delves into"
- Mention one concrete angle (fraud, policy, product, users, money, risk)
- Write as if explaining to a smart Instagram audience

EXAMPLE:
{{
  "kya_hua": "The company announced a new AI feature for its main product.",
  "kyun_important": "This could change how users interact with the platform."
}}

NEWS:
Title: {article["title"]}
Summary: {article["summary"]}
"""

    raw = llm_call(prompt)

    try:
        data = json.loads(raw)

        # 🔒 Final safety (never allow empty)
        if not data.get("kya_hua") or not data.get("kyun_important"):
            raise ValueError("Empty fields")

        return data

    except Exception:
        return {
            "kya_hua": "The article reports a recent development related to this topic.",
            "kyun_important": "This update could influence users, companies, or the broader tech industry."
        }
