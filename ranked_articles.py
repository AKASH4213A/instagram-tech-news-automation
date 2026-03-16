# engine v2

import re
from datetime import datetime


HIGH_IMPACT = ["launch", "releases", "raises", "funding", "acquires", "acquisition"]
AI_KEYWORDS = ["ai", "openai", "chatgpt", "model"]
BIG_TECH = ["google", "apple", "microsoft", "amazon", "meta", "tesla"]
LOW_IMPACT = ["opinion", "blog", "how to", "guide", "explained"]

#fixing substring bug
#Snap Q4 news → galti se AI tag → AI score → AI bucket
def has_word(text, word):
    return re.search(rf"\b{word}\b", text) is not None



def score_article(article):
    score = 0
    title = article["title"].lower()

    for kw in HIGH_IMPACT:
        if kw in title:
            score += 4

    for kw in AI_KEYWORDS:
        if has_word(title, kw):
            score += 3

    for kw in BIG_TECH:
        if kw in title:
            score += 2

    for kw in LOW_IMPACT:
        if kw in title:
            score -= 3

    score += 2  # source weight

    if article["published"] != "unknown":
        try:
            days_old = (datetime.now() -
                        datetime.strptime(article["published"], "%Y-%m-%d")).days
            score += max(0, 3 - days_old)
        except:
            pass

    return score

# for keyword returning
def detect_topic(article):
    title = article["title"].lower()

    if any(x in title for x in ["q1", "q2", "q3", "q4", "earnings", "revenue"]):
        return "BUSINESS"

    if any(has_word(title, k) for k in AI_KEYWORDS):
        return "AI"

    if any(has_word(title, k) for k in BIG_TECH):
        return "BIG_TECH"

    if "startup" in title or "funding" in title or "raises" in title:
        return "STARTUP"

    if any(x in title for x in ["hack", "breach", "vulnerability", "security"]):
        return "SECURITY"

    if any(x in title for x in ["phone", "laptop", "device", "wearable"]):
        return "GADGETS"

    return "OTHER"


# for balanced Topic encountering the major same topics
def pick_top_7_by_topic(articles):
    best_per_topic = {}

    for article in articles:
        topic = detect_topic(article)
        score = score_article(article)

# Agar topic pehle se nahi aaya
        if topic not in best_per_topic:
            best_per_topic[topic] = (score, article)
        else:
# Compare score, jo better ho wo rakho
            if score > best_per_topic[topic][0]:
                best_per_topic[topic] = (score, article)

# Sirf article objects nikaalo
    result = [item[1] for item in best_per_topic.values()]

# Score ke hisaab se sort (optional, for display)
    result.sort(key=score_article, reverse=True)

# Max 7 hi return karo
    return result[:7]

