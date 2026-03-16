import re

def generate_headline(article, summary_data=None):
    title = article["title"]

    # remove quotes
    title = title.replace("‘", "").replace("’", "").replace('"', "")

    # remove filler phrases
    fillers = [
        "is working to",
        "better than any show on tv right now",
        "right now",
        "is reportedly",
        "according to",
    ]

    lowered = title.lower()
    for f in fillers:
        lowered = lowered.replace(f, "")

    # clean spaces
    cleaned = " ".join(lowered.split())

    # capitalize first letter
    cleaned = cleaned[0].upper() + cleaned[1:]

    # limit length (Instagram-friendly)
    words = cleaned.split()
    if len(words) > 8:
        cleaned = " ".join(words[:8])

    return cleaned
