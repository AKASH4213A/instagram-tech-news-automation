import random
from caption_bank import CAPTION_TEMPLATES

def generate_caption(article, summary_data):
    topic = article.get("topic", "OTHER")
    templates = CAPTION_TEMPLATES.get(topic, CAPTION_TEMPLATES["OTHER"])

# Pick viral hook randomly
    hook = random.choice(templates)

# News-specific line (from kya_hua)
    context = summary_data.get("kya_hua", "").strip()

    if len(context.split()) > 14:
        context = " ".join(context.split()[:14]) + "..."

# Soft CTA
    cta = "Swipe karke poora samjho →"

    return f"{hook}\n{context}\n\n{cta}"
