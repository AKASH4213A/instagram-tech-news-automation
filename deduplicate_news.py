from difflib import SequenceMatcher

def is_similar(title1, title2, threshold=0.75):
    return SequenceMatcher(None, title1.lower(), title2.lower()).ratio() > threshold


def deduplicate_news(articles):
    unique_articles = []

    for article in articles:
        duplicate_found = False

        for existing in unique_articles:
            if is_similar(article["title"], existing["title"]):
                duplicate_found = True
                break

        if not duplicate_found:
            unique_articles.append(article)

    return unique_articles
